# =============================================================================
# routers/rotas.py — Os 5 endpoints CRUD de Rotas de Transporte
# =============================================================================
#
# ESTE É O SEU PRINCIPAL DESAFIO.
#
# Você deve implementar o corpo (a lógica) de cada um dos 5 endpoints abaixo.
# A estrutura já está pronta: nome da função, rota HTTP, parâmetros e
# tipo de retorno. Você só precisa substituir o "pass" pela lógica correta.
#
# O que você tem disponível:
#   - db: Session → a sessão do banco de dados (use para buscar, salvar, etc.)
#   - RotaTransporte → o model do banco (importado de app.models)
#   - RotaCreate, RotaUpdate, RotaResponse → schemas Pydantic (de app.schemas)
#   - HTTPException → para retornar erros (ex: 404 quando rota não existe)
#
# Operações disponíveis no db:
#   db.query(RotaTransporte).all()           → busca todos
#   db.query(RotaTransporte).filter(...).all() → busca com filtro
#   db.get(RotaTransporte, id)              → busca por ID (retorna None se não existe)
#   db.add(objeto)                          → prepara para salvar
#   db.commit()                             → confirma e salva no banco
#   db.refresh(objeto)                      → atualiza o objeto com dados do banco
#
# DICA: Use .model_dump() para converter schemas Pydantic em dicionário.
#       NÃO use .dict() — está obsoleto no Pydantic v2.
# =============================================================================

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import RotaTransporte
from app.schemas import RotaCreate, RotaResponse, RotaUpdate

# O router agrupa todos os endpoints deste arquivo.
# O prefixo "/rotas" e a tag "Rotas" são definidos aqui.
router = APIRouter(prefix="/rotas", tags=["Rotas"])


# =============================================================================
# GET /rotas — Lista todas as rotas ATIVAS
# =============================================================================
#
# Retorna uma lista de todas as rotas onde ativa == True.
# Se não houver nenhuma rota, retorna uma lista vazia [].
#
# TODO: Implemente a busca.
#
# Dica:
#   db.query(RotaTransporte).filter(RotaTransporte.ativa == True).all()
# =============================================================================
@router.get("/", response_model=list[RotaResponse])
def listar_rotas(db: Session = Depends(get_db)):
    # TODO: buscar todas as rotas ativas no banco e retornar a lista
    pass


# =============================================================================
# GET /rotas/{id} — Busca uma rota específica pelo ID
# =============================================================================
#
# Retorna a rota com o ID fornecido.
# Se o ID não existir OU a rota estiver inativa (ativa == False), retorna 404.
#
# TODO: Implemente a busca e a verificação de existência.
#
# Dica:
#   rota = db.get(RotaTransporte, id)
#   if not rota or not rota.ativa:
#       raise HTTPException(status_code=404, detail="Rota não encontrada")
#   return rota
# =============================================================================
@router.get("/{id}", response_model=RotaResponse)
def buscar_rota(id: int, db: Session = Depends(get_db)):
    # TODO: buscar a rota pelo id, verificar se existe e se está ativa, retornar
    pass


# =============================================================================
# POST /rotas — Cria uma nova rota
# =============================================================================
#
# Recebe os dados do body (JSON), cria uma nova rota no banco e retorna ela.
# O status code de sucesso é 201 (Created), não 200.
#
# TODO: Implemente a criação.
#
# Dica — passo a passo:
#   1. Criar o objeto: rota = RotaTransporte(**dados.model_dump())
#   2. Adicionar ao banco: db.add(rota)
#   3. Confirmar: db.commit()
#   4. (já feito abaixo) db.refresh(rota) — não remova, é necessário
#   5. return rota
#
# ATENÇÃO: O db.refresh(rota) já está presente. Não remova.
# Ele atualiza o objeto com os dados gerados pelo banco (id, criada_em).
# =============================================================================
@router.post("/", response_model=RotaResponse, status_code=201)
def criar_rota(dados: RotaCreate, db: Session = Depends(get_db)):
    # TODO: criar o objeto RotaTransporte, adicionar ao banco e commitar
    rota = None  # ← substitua esta linha pela criação real

    db.refresh(rota)  # ← não remova esta linha
    return rota


# =============================================================================
# PUT /rotas/{id} — Atualiza uma rota existente
# =============================================================================
#
# Recebe os campos a atualizar (todos opcionais em RotaUpdate).
# Se o ID não existir ou a rota estiver inativa, retorna 404.
#
# TODO: Implemente a atualização.
#
# Dica — passo a passo:
#   1. Buscar a rota: rota = db.get(RotaTransporte, id)
#   2. Verificar se existe e está ativa (retornar 404 se não)
#   3. Atualizar os campos que vieram:
#      for campo, valor in dados.model_dump(exclude_unset=True).items():
#          setattr(rota, campo, valor)
#   4. db.commit()
#   5. (já feito abaixo) db.refresh(rota)
#   6. return rota
#
# O exclude_unset=True garante que só os campos enviados pelo usuário
# sejam atualizados — os campos não enviados ficam como estão.
#
# ATENÇÃO: O db.refresh(rota) já está presente. Não remova.
# =============================================================================
@router.put("/{id}", response_model=RotaResponse)
def atualizar_rota(id: int, dados: RotaUpdate, db: Session = Depends(get_db)):
    # TODO: buscar a rota, verificar se existe, atualizar os campos e commitar
    rota = None  # ← substitua pela busca real

    db.refresh(rota)  # ← não remova esta linha
    return rota


# =============================================================================
# DELETE /rotas/{id} — Desativa uma rota (soft delete)
# =============================================================================
#
# NÃO apaga do banco — apenas muda ativa para False.
# Isso se chama "soft delete": a rota continua no banco, mas não aparece
# nas listagens nem pode ser buscada pelo GET /rotas/{id}.
#
# Se o ID não existir ou já estiver inativo, retorna 404.
#
# TODO: Implemente o soft delete.
#
# Dica — passo a passo:
#   1. Buscar a rota: rota = db.get(RotaTransporte, id)
#   2. Verificar se existe e está ativa (retornar 404 se não)
#   3. rota.ativa = False
#   4. db.commit()
#   5. return {"ok": True}
# =============================================================================
@router.delete("/{id}")
def deletar_rota(id: int, db: Session = Depends(get_db)):
    # TODO: buscar a rota, verificar se existe, setar ativa=False e commitar
    pass
