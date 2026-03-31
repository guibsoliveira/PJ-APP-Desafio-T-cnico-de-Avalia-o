# =============================================================================
# tests/test_rotas.py — Testes dos endpoints de Rotas
# =============================================================================
#
# PARTE DESTE ARQUIVO É O SEU DESAFIO.
#
# O que é um teste automatizado?
#   É uma função que verifica automaticamente se o código funciona.
#   O pytest procura funções que começam com "test_" e as executa.
#   Se todos os "assert" passarem → teste VERDE.
#   Se algum "assert" falhar → teste VERMELHO com a linha exata do erro.
#
# Como rodar os testes:
#   pytest -v
#   O -v (verbose) mostra o nome de cada teste e se passou ou falhou.
#
# Como funciona a fixture "client"?
#   Você não precisa criar nada — basta colocar "client" como parâmetro
#   da função de teste. O pytest injeta automaticamente o TestClient
#   configurado em conftest.py com banco em memória.
#
# Como fazer requisições nos testes:
#   client.get("/rotas")                      → GET /rotas
#   client.post("/rotas", json={...})         → POST /rotas com dados
#   client.put("/rotas/1", json={...})        → PUT /rotas/1
#   client.delete("/rotas/1")                 → DELETE /rotas/1
#
# O que verificar:
#   response.status_code → o número HTTP (200, 201, 404, etc.)
#   response.json()      → o corpo da resposta convertido em dicionário Python
# =============================================================================

# Dados de exemplo que serão usados nos testes
# Fique à vontade para mudar os valores
DADOS_ROTA = {
    "nome": "Rota Centro",
    "escola_destino": "Escola Municipal João Paulo",
    "horario_saida": "07:00",
    "horario_retorno": "17:30",
    "descricao": "Rota que passa pelo centro da cidade",
}


# =============================================================================
# Teste 1: Criar uma rota com sucesso
# =============================================================================
#
# O que este teste verifica:
#   Quando fazemos POST /rotas com dados válidos, a API deve:
#   - Retornar status code 201 (Created)
#   - Retornar os dados da rota criada, incluindo o "id" gerado
#   - O campo "nome" deve ser igual ao que foi enviado
#   - O campo "ativa" deve ser True por padrão
#
# TODO: Complete os asserts abaixo.
#
# Dica — o que verificar:
#   assert response.status_code == 201
#   assert response.json()["nome"] == DADOS_ROTA["nome"]
#   assert response.json()["ativa"] == True
#   assert "id" in response.json()
# =============================================================================
def test_criar_rota(client):
    response = client.post("/rotas/", json=DADOS_ROTA)

    # TODO: verifique o status code (deve ser 201)
    # TODO: verifique que o campo "nome" está correto
    # TODO: verifique que o campo "ativa" é True
    # TODO: verifique que o campo "id" existe na resposta


# =============================================================================
# Teste 2: Buscar uma rota que não existe
# =============================================================================
#
# O que este teste verifica:
#   Quando fazemos GET /rotas/999 (ID que não existe), a API deve:
#   - Retornar status code 404 (Not Found)
#
# TODO: Complete o assert abaixo.
#
# Dica:
#   assert response.status_code == 404
# =============================================================================
def test_rota_nao_encontrada(client):
    response = client.get("/rotas/999")

    # TODO: verifique que o status code é 404


# =============================================================================
# Teste 3: Deletar uma rota e verificar que ela some
# =============================================================================
#
# O que este teste verifica:
#   1. Primeiro cria uma rota com POST
#   2. Pega o ID da rota criada
#   3. Faz DELETE nessa rota
#   4. Tenta buscar a rota deletada com GET
#   5. A rota deletada deve retornar 404 (soft delete funciona)
#
# Este teste valida a decisão de design mais importante do desafio:
# o DELETE não apaga do banco — ele apenas muda "ativa" para False.
# Depois disso, GET /rotas/{id} deve retornar 404 para essa rota.
#
# TODO: Complete os asserts abaixo.
#
# Dica:
#   # Criar a rota
#   criar_response = client.post("/rotas/", json=DADOS_ROTA)
#   id_criado = criar_response.json()["id"]
#
#   # Deletar
#   delete_response = client.delete(f"/rotas/{id_criado}")
#   assert delete_response.status_code == 200
#
#   # Verificar que sumiu
#   get_response = client.get(f"/rotas/{id_criado}")
#   assert get_response.status_code == 404
# =============================================================================
def test_deletar_rota(client):
    # Passo 1: criar uma rota para ter algo para deletar
    criar_response = client.post("/rotas/", json=DADOS_ROTA)
    id_criado = criar_response.json()["id"]

    # TODO: fazer o DELETE na rota criada e verificar status 200

    # TODO: buscar a rota deletada e verificar que retorna 404
