# playlists-recommender-system

Sistema de recomendação de playlists baseado em **FastAPI**.  
Dado o conteúdo de uma playlist (músicas, gêneros, artistas, etc.), o sistema gera sugestões automáticas de novas músicas que se encaixam no mesmo perfil.

## 🚀 Visão geral

O projeto implementa uma API REST moderna utilizando **FastAPI**, **Python 3** e **machine learning / filtragem colaborativa** para gerar recomendações musicais.  

A documentação interativa é gerada automaticamente em:

- Swagger UI → [`/docs`](http://localhost:50000/docs)
- ReDoc → [`/redoc`](http://localhost:50000/redoc)


---

## 📂 Estrutura do repositório

| Arquivo / Pasta | Descrição |
|---|---|
| `app.py` | Aplicação principal (API / interface) para interagir com o sistema de recomendação. |
| `Dockerfile` | Arquivo para criação da imagem Docker do projeto. |
| `requirements.txt` | Dependências Python necessárias. |
| `.github/workflows/` | Workflow(s) de CI/CD para automação. |
| `README.md` | Este arquivo de apresentação e instruções. |

---

## 🚀 Funcionalidades

- Recebe uma playlist (lista de faixas ou identificadores) como entrada.  
- Gera recomendações de músicas que “combinam” com aquela playlist.  
- Pode ser executado localmente ou dentro de um container Docker.  

---

## 🛠️ Requisitos / Dependências

- Python 3.x  
- Bibliotecas listadas em `requirements.txt`  
- (Opcional) Docker para execução em container  

Para instalar dependências:

```bash
pip install -r requirements.txt
```
---

## 🧭 Endpoints disponíveis

| Método | Rota | Descrição | Corpo da Requisição | Exemplo de Resposta |
|:--------|:------|:------------|:--------------------|:--------------------|
| `GET` | `/healthz` | Verifica se a API está operacional. | — | `{"status":"ok","model":"2025-10-22 23:20:47"}` |
| `POST` | `/recommend/api` | Gera recomendações de músicas baseadas na playlist enviada. | `{"liked_songs": ["One Dance","Closer","Roses"]}` | `{"song": ["What Do You Mean?","Treat You Better"],"version": "2.0.0","model": "2025-10-22 23:20:47"}` |
| `GET` | `/docs` | Interface interativa Swagger UI gerada automaticamente pelo FastAPI. | — | Interface web interativa |
| `GET` | `/redoc` | Documentação ReDoc alternativa, gerada automaticamente. | — | Interface web de documentação |
| `GET` | `/openapi.json` | Retorna o schema OpenAPI completo da API. | — | JSON com a definição OpenAPI |

---

## 🐳 Uso com Docker

Para executar o projeto em um container Docker, siga os passos abaixo:

1. **Construir a imagem Docker:**

```bash
docker build -t playlists-recommender .
```

2. **Executar o container:**

```bash
docker run -p 50000:8000 playlists-recommender
```

O sistema estará disponível em `http://localhost:50000`.


