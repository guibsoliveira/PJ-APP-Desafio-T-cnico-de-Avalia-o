# =============================================================================
# tests/conftest.py — Configuração compartilhada dos testes
# =============================================================================
#
# ESTE ARQUIVO ESTÁ COMPLETO. NÃO MODIFIQUE.
#
# O que este arquivo faz:
#   Define "fixtures" do pytest — são funções de setup compartilhadas entre testes.
#
# O que é uma fixture?
#   É uma função que prepara algo antes do teste rodar.
#   O pytest injeta a fixture automaticamente quando o teste pede pelo nome.
#
# A fixture "client" deste arquivo:
#   1. Cria um banco de dados em MEMÓRIA (não no disco) apenas para os testes
#   2. Cria todas as tabelas nesse banco temporário
#   3. Substitui o banco real pelo banco de teste
#   4. Cria um TestClient (cliente HTTP falso para simular requisições)
#   5. Ao final do teste, descarta tudo — próximo teste começa limpo
#
# Por que banco em memória nos testes?
#   - Mais rápido (sem I/O de disco)
#   - Não polui o banco de desenvolvimento
#   - Cada teste começa com banco vazio e isolado
# =============================================================================

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

# Banco de dados em memória exclusivo para os testes
# "sqlite:///:memory:" = banco que vive na RAM, some ao fechar
SQLALCHEMY_TEST_URL = "sqlite:///:memory:"

engine_test = create_engine(
    SQLALCHEMY_TEST_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Necessário para SQLite em memória com testes
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_test
)


def override_get_db():
    """Substitui o banco real pelo banco de teste."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    """
    Fixture principal dos testes.

    Cria um TestClient com banco em memória isolado.
    Cada teste que pede 'client' recebe um banco limpo.

    Como usar nos testes:
        def test_meu_teste(client):
            response = client.get("/rotas")
            ...
    """
    # Cria as tabelas no banco de teste
    Base.metadata.create_all(bind=engine_test)

    # Substitui a dependência de banco real pelo banco de teste
    app.dependency_overrides[get_db] = override_get_db

    # Cria o cliente HTTP de teste
    with TestClient(app) as test_client:
        yield test_client

    # Limpa: remove todas as tabelas ao final do teste
    Base.metadata.drop_all(bind=engine_test)

    # Remove o override para não interferir em outros testes
    app.dependency_overrides.clear()
