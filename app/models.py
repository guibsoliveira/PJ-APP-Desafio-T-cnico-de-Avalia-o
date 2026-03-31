# =============================================================================
# models.py — Modelo do banco de dados (SQLAlchemy)
# =============================================================================
#
# ESTE ARQUIVO ESTÁ COMPLETO. NÃO MODIFIQUE.
#
# O que é um "model" SQLAlchemy?
#   É uma classe Python que representa uma tabela no banco de dados.
#   Cada atributo da classe vira uma coluna na tabela.
#   O SQLAlchemy traduz operações em Python para SQL automaticamente.
#
# ATENÇÃO: Este arquivo define a ESTRUTURA DA TABELA no banco.
#   Não confunda com o schemas.py, que define o que a API recebe e retorna.
#   São coisas diferentes com propósitos diferentes.
#
#   models.py  → estrutura do banco de dados (SQLAlchemy)
#   schemas.py → estrutura dos dados da API (Pydantic)
# =============================================================================

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class RotaTransporte(Base):
    """
    Representa uma rota de transporte escolar no banco de dados.

    Tabela criada automaticamente como "rotas_transporte" no arquivo desafio.db.
    """

    # Nome da tabela no banco de dados
    __tablename__ = "rotas_transporte"

    # Identificador único — gerado automaticamente pelo banco (autoincrement)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # Nome da rota — obrigatório
    nome: Mapped[str] = mapped_column(String(200), nullable=False)

    # Descrição opcional — pode ser None (NULL no banco)
    descricao: Mapped[str] = mapped_column(Text, nullable=True, default=None)

    # Escola de destino — obrigatório
    escola_destino: Mapped[str] = mapped_column(String(200), nullable=False)

    # Horário de saída — string no formato "07:30"
    horario_saida: Mapped[str] = mapped_column(String(5), nullable=False)

    # Horário de retorno — string no formato "17:30"
    horario_retorno: Mapped[str] = mapped_column(String(5), nullable=False)

    # Se a rota está ativa — True por padrão
    # DELETE não apaga do banco: apenas muda ativa para False (soft delete)
    ativa: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Data/hora de criação — gerada automaticamente pelo Python no momento do insert
    criada_em: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
