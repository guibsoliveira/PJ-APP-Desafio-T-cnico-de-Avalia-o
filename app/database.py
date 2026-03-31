# =============================================================================
# database.py — Conexão com o banco de dados
# =============================================================================
#
# ESTE ARQUIVO ESTÁ COMPLETO. NÃO MODIFIQUE.
#
# O que este arquivo faz:
#   1. Cria um arquivo "desafio.db" na pasta do projeto (banco SQLite)
#   2. Cria todas as tabelas automaticamente na primeira vez que rodar
#   3. Fornece a função get_db() que os endpoints usam para falar com o banco
#
# O banco SQLite é um arquivo único (.db) que não precisa de nenhuma
# instalação separada — já vem com o Python.
# =============================================================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL do banco: "sqlite:///./desafio.db" significa um arquivo chamado
# "desafio.db" na pasta atual do projeto.
DATABASE_URL = "sqlite:///./desafio.db"

# O engine é o "motor" que conecta ao banco.
# check_same_thread=False é necessário apenas para SQLite com FastAPI.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# SessionLocal é a "fábrica" de sessões.
# Cada request HTTP abre uma sessão nova e fecha ao terminar.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base é a classe que todos os modelos SQLAlchemy herdam.
# Quando chamamos Base.metadata.create_all(), ela cria as tabelas no banco.
class Base(DeclarativeBase):
    pass


# =============================================================================
# get_db — Dependência injetada nos endpoints
# =============================================================================
#
# NÃO MODIFIQUE ESTA FUNÇÃO.
#
# O "yield" aqui é especial: o FastAPI abre a sessão ANTES do endpoint rodar
# e a fecha DEPOIS — mesmo que o endpoint dê erro. Isso garante que a conexão
# com o banco nunca fique aberta por acidente.
#
# Nos endpoints, você vai ver: db: Session = Depends(get_db)
# Isso significa: "antes de executar este endpoint, chame get_db() e injete
# o resultado como o parâmetro db".
# =============================================================================
def get_db():
    db = SessionLocal()
    try:
        yield db  # ← o endpoint roda aqui, usando o db
    finally:
        db.close()  # ← sempre fecha, mesmo se der erro
