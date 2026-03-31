# =============================================================================
# main.py — Ponto de entrada da API
# =============================================================================
#
# ESTE ARQUIVO ESTÁ COMPLETO. NÃO MODIFIQUE.
#
# O que este arquivo faz:
#   1. Cria o app FastAPI com título e descrição
#   2. Cria as tabelas no banco na primeira vez que a API sobe
#   3. Registra o router de rotas (os 5 endpoints que você vai implementar)
#   4. Adiciona um endpoint /health para verificar se a API está no ar
#
# Como subir a API:
#   uvicorn app.main:app --reload
#
# Como acessar a documentação automática:
#   http://127.0.0.1:8000/docs  ← interface visual para testar os endpoints
#   http://127.0.0.1:8000/redoc ← documentação alternativa
# =============================================================================

from fastapi import FastAPI

from app.database import Base, engine
from app.routers import rotas

# Cria todas as tabelas definidas nos models, se ainda não existirem.
# Na primeira execução, cria o arquivo desafio.db e a tabela rotas_transporte.
Base.metadata.create_all(bind=engine)

# Inicializa o app FastAPI
app = FastAPI(
    title="PJ-APP — Desafio de Avaliação",
    description="API de gerenciamento de Rotas de Transporte Escolar",
    version="0.1.0",
)

# Registra o router de rotas com prefixo /rotas
# Isso significa que todos os endpoints em rotas.py ficam disponíveis em /rotas
app.include_router(rotas.router)


# Endpoint de health check — verifica se a API está no ar
# Acesse: http://127.0.0.1:8000/health
@app.get("/health", tags=["Status"])
def health_check():
    return {"status": "ok"}
