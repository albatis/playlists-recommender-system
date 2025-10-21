import os
import pickle
import time
from datetime import datetime
from typing import List, Set

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_PATH = os.getenv('OUTPUT_MODEL_PATH', '/mnt/association_rules.pkl')
API_VERSION = "2.0.0"

rules: pd.DataFrame = None
model_updated_at: str = "Modelo não carregado"

class RecommendationRequest(BaseModel):
    liked_songs: List[str]

class RecommendationResponse(BaseModel):
    song: List[str]
    version: str
    model: str

app = FastAPI(title="API de Recomendação de Músicas (v2)", version=API_VERSION, 
              description="API para recomendar músicas usando regras de associação, aceitando uma lista de músicas por POST."
)

def load_model():
    global rules, model_updated_at
    try:
        if not os.path.exists(MODEL_PATH):
            print(f"ERRO: Arquivo não foi encontrado [{MODEL_PATH}]")
            return
        with open(MODEL_PATH, 'rb') as f:
            loaded_rules = pickle.load(f)
        rules = loaded_rules
    except Exception as e:
        print(f"ERRO: não foi possível carregar o modelo {e}")
        rules = None
        return

    try:
        timestamp_s = os.path.getmtime(MODEL_PATH)
        model_updated_at = datetime.fromtimestamp(timestamp_s).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{len(rules)} regras encontradas. Atualizado em: {model_updated_at}")
    except Exception:
        model_updated_at = "Timestamp indisponível"


def get_recommendations_from_rules(input_songs: List[str], max_results: int = 10) -> List[str]:
    if rules is None or rules.empty:
        return []
    recommended_songs: Set[str] = set()
    input_set = set(input_songs)
    for song in input_set:
        matching_rules = rules[rules['antecedents'].apply(lambda x: song in x)]
        for consequent_set in matching_rules['consequents']:
            recommended_songs.update(consequent_set)
    recommended_songs -= input_set
    return list(recommended_songs)[:max_results]

@app.on_event("startup")
def startup_event():
    load_model()

@app.post("/api/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest):
    if rules is None:
        raise HTTPException(status_code=503, detail="O modelo de recomendação não está disponível ou não foi carregado corretamente.")
    input_songs = request.liked_songs
    if not input_songs:
        return RecommendationResponse(song=[], version=API_VERSION, model=model_updated_at)
    recommended_songs = get_recommendations_from_rules(input_songs, max_results=10)
    response_data = {"song": recommended_songs, "version": API_VERSION, "model": model_updated_at }
    return response_data
