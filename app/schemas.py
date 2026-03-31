# =============================================================================
# schemas.py — Schemas de validação da API (Pydantic)
# =============================================================================
#
# PARTE DESTE ARQUIVO É O SEU DESAFIO. Leia tudo antes de começar.
#
# O que é Pydantic?
#   É uma biblioteca de validação de dados. Quando alguém faz um POST na API,
#   o Pydantic verifica se os dados vieram corretos antes de qualquer outra coisa.
#   Se faltar um campo obrigatório, ele devolve um erro 422 automaticamente.
#
# Por que schemas separados do model do banco (models.py)?
#   O model do banco tem campos gerados automaticamente (id, criada_em, ativa).
#   O usuário não manda esses campos — o servidor cria.
#   Por isso separamos:
#     RotaCreate   → o que o usuário manda no POST (sem id, sem criada_em)
#     RotaUpdate   → o que o usuário pode atualizar no PUT (todos opcionais)
#     RotaResponse → o que a API devolve (com id e criada_em)
#
# DICA IMPORTANTE:
#   Use .model_dump() para converter um schema em dicionário.
#   NÃO use .dict() — essa forma antiga não funciona mais no Pydantic v2.
# =============================================================================

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# =============================================================================
# RotaCreate — dados que o usuário manda para CRIAR uma rota (POST /rotas)
# =============================================================================
#
# TODO: Defina os campos que o usuário deve enviar para criar uma rota.
#
# Campos obrigatórios (sem valor padrão): o usuário PRECISA mandar
# Campos opcionais (com = None): o usuário PODE mandar, mas não é obrigado
#
# Exemplo de como definir campos:
#   nome: str                        ← obrigatório, texto
#   escola_destino: str              ← obrigatório, texto
#   horario_saida: str               ← obrigatório, texto (ex: "07:30")
#   descricao: Optional[str] = None  ← opcional, texto ou None
#
# Campos que NÃO devem estar aqui: id, ativa, criada_em
# (esses são gerados automaticamente — o usuário não manda)
# =============================================================================
class RotaCreate(BaseModel):
    # TODO: adicione os campos aqui
    pass


# =============================================================================
# RotaUpdate — dados que o usuário pode mandar para ATUALIZAR uma rota (PUT)
# =============================================================================
#
# TODO: Defina os campos que podem ser atualizados.
#
# No PUT, todos os campos são OPCIONAIS — o usuário pode mandar só o que
# quer mudar. Por isso todos têm = None como padrão.
#
# Use Optional[tipo] = None para todos os campos.
#
# Exemplo:
#   nome: Optional[str] = None
#   escola_destino: Optional[str] = None
# =============================================================================
class RotaUpdate(BaseModel):
    # TODO: adicione os campos aqui
    pass


# =============================================================================
# RotaResponse — o que a API devolve em todas as respostas
# =============================================================================
#
# ESTE SCHEMA ESTÁ COMPLETO. Não modifique.
#
# Inclui todos os campos que a API retorna, incluindo id e criada_em
# que são gerados automaticamente.
#
# model_config com from_attributes=True permite que o Pydantic leia
# objetos SQLAlchemy diretamente (sem precisar converter para dicionário).
# =============================================================================
class RotaResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    escola_destino: str
    horario_saida: str
    horario_retorno: str
    ativa: bool
    criada_em: datetime

    model_config = {"from_attributes": True}
