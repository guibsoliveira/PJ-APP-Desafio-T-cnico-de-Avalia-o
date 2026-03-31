# INSTRUCIONAL — Guia Completo para o Guilherme

> Este arquivo é **só para você**. Os meninos não precisam ler isso.
> Aqui está tudo que você precisa saber para entender cada arquivo do template,
> como verificar se está funcionando, e o que observar na avaliação.

---

## Seção 1 — Verificar e instalar Python

### O que é Python aqui

Python é a linguagem de programação que usamos. A versão importa porque recursos
como `list[RotaResponse]` (tipagem moderna) só funcionam no Python 3.9+.
Usamos 3.11+ para garantir compatibilidade com todas as bibliotecas.

### Passo a passo para verificar

1. Abrir o VS Code
2. Pressionar `Ctrl + \`` (acento grave) para abrir o terminal integrado
3. Digitar e pressionar Enter:
   ```
   python --version
   ```
4. **Se aparecer** `Python 3.11.x` ou superior → tudo certo, vá para Seção 2
5. **Se aparecer** "não reconhecido como comando interno":
   - Acessar [python.org/downloads](https://python.org/downloads)
   - Baixar Python 3.11 ou superior (botão amarelo grande)
   - Durante a instalação: **marcar "Add Python to PATH"** (caixa no rodapé da tela)
   - Concluir instalação
   - **Fechar e reabrir o VS Code completamente**
   - Repetir o passo 3

### Como verificar no VS Code também

No canto inferior direito do VS Code, aparece a versão do Python selecionada.
Clique nela para escolher o Python 3.11+ se houver mais de uma versão instalada.

---

## Seção 2 — Ambiente virtual (venv)

### O que é e por que existe

Imagine que você instala o FastAPI globalmente no Python da sua máquina.
Depois cria outro projeto que precisa de uma versão diferente do FastAPI.
Conflito. O venv resolve isso criando uma "bolha" isolada por projeto.

Cada projeto tem seu próprio venv com suas próprias versões de bibliotecas.
O Python global da máquina fica intocado.

### Passo a passo para criar

Na pasta do projeto, com o terminal aberto:

```
python -m venv venv
```

Isso cria uma pasta chamada `venv/` no projeto com um Python e pip próprios.

### Passo a passo para ativar (Windows)

**PowerShell** (mais comum no VS Code):
```
.\venv\Scripts\Activate.ps1
```

**CMD (Prompt de Comando)**:
```
venv\Scripts\activate.bat
```

**Se o PowerShell der erro de permissão** (`cannot be loaded because running scripts is disabled`):
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Responda `S` quando perguntar. Depois ative novamente.

### Como saber que funcionou

O terminal passa a mostrar `(venv)` no início de cada linha:
```
(venv) PS C:\Users\Guilherme\Desktop\IA\pjapp-desafio-template>
```

### Por que a pasta venv está no .gitignore

A pasta `venv/` tem centenas de megabytes. Não faz sentido subir para o GitHub.
Qualquer pessoa que clonar o repo reinstala com `pip install -r requirements.txt`.

---

## Seção 3 — Dependências (requirements.txt)

### O que é

Uma lista de pacotes Python com versões fixas. Garante que todos usem
exatamente as mesmas versões, evitando o "funciona na minha máquina".

### Passo a passo para instalar

Com o venv **ativado** (você vê `(venv)` no terminal):
```
pip install -r requirements.txt
```

### Verificar que funcionou

```
pip list
```

Deve aparecer na lista: fastapi, uvicorn, sqlalchemy, pydantic, pytest, httpx, ruff, black.

### O que cada pacote faz

| Pacote | Função |
|--------|--------|
| `fastapi` | Framework que cria a API REST |
| `uvicorn` | Servidor que executa o FastAPI localmente |
| `sqlalchemy` | ORM — conversa com o banco de dados usando Python |
| `pydantic` | Valida os dados recebidos e enviados pela API |
| `pytest` | Executa os testes automatizados |
| `httpx` | Permite fazer requisições HTTP dentro dos testes |
| `ruff` | Linter — detecta erros e problemas sem executar o código |
| `black` | Formatter — formata o código automaticamente |

---

## Seção 4 — Estrutura de pastas

```
pjapp-desafio-template/
│
├── README.md           → Instruções do desafio (os meninos leem)
├── INSTRUCIONAL.md     → Este guia (só você)
├── requirements.txt    → Lista de dependências
├── pyproject.toml      → Configuração do Ruff e Black
├── .gitignore          → Arquivos que o Git não rastreia
│
├── app/
│   ├── __init__.py     → Arquivo vazio, obrigatório — marca a pasta como módulo Python
│   ├── main.py         → Ponto de entrada — inicializa o app e registra as rotas
│   ├── database.py     → Conexão com o banco SQLite
│   ├── models.py       → Estrutura da tabela no banco (SQLAlchemy)
│   ├── schemas.py      → Estrutura dos dados da API (Pydantic) ← ELES PREENCHEM
│   └── routers/
│       ├── __init__.py → Arquivo vazio, obrigatório
│       └── rotas.py    → Os 5 endpoints CRUD ← ELES PREENCHEM
│
└── tests/
    ├── __init__.py     → Arquivo vazio, obrigatório
    ├── conftest.py     → Setup dos testes (banco em memória, client HTTP)
    └── test_rotas.py   → Os 3 testes ← ELES COMPLETAM OS ASSERTS
```

### Por que existem arquivos `__init__.py` vazios?

O Python precisa deles para reconhecer a pasta como um "módulo" importável.
Sem eles, `from app.models import RotaTransporte` não funciona.
São arquivos vazios — não precisam de conteúdo.

---

## Seção 5 — O que é FastAPI

### Em linguagem simples

FastAPI é um framework que transforma funções Python em endpoints HTTP.

Você escreve isso:
```python
@app.get("/rotas")
def listar():
    return [{"nome": "Rota Centro"}]
```

E o FastAPI cria automaticamente:
- Um endpoint em `GET http://127.0.0.1:8000/rotas`
- Documentação interativa em `/docs`
- Validação automática de tipos

### Como subir a API

Com venv ativado, na pasta do projeto:
```
uvicorn app.main:app --reload
```

O que cada parte significa:
- `uvicorn` → o servidor
- `app.main` → o arquivo `app/main.py`
- `:app` → a variável `app` dentro desse arquivo (o objeto FastAPI)
- `--reload` → reinicia automaticamente quando você salva um arquivo

### Verificar que funcionou

Deve aparecer no terminal:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Abrir no browser: `http://127.0.0.1:8000/docs`

Vai aparecer o Swagger UI — uma interface gráfica para testar os endpoints.
Você pode fazer POST, GET, DELETE diretamente pelo browser sem precisar do Postman.

---

## Seção 6 — Métodos HTTP e status codes

### O que são métodos HTTP

Toda comunicação na web usa verbos que indicam o que está sendo feito:

| Método | Significa | Analogia do mundo real |
|--------|-----------|----------------------|
| `GET` | Quero buscar algo | "Me mostra a lista de rotas" |
| `POST` | Quero criar algo novo | "Cria uma nova rota com esses dados" |
| `PUT` | Quero atualizar algo existente | "Muda o horário desta rota" |
| `DELETE` | Quero remover algo | "Desativa esta rota" |

### Status codes — o que os números significam

A API sempre responde com um número que indica o resultado:

| Código | Nome | Quando usar |
|--------|------|-------------|
| 200 | OK | GET ou DELETE funcionaram |
| 201 | Created | POST criou algo com sucesso |
| 404 | Not Found | Buscou algo que não existe |
| 422 | Unprocessable Entity | Dados enviados estão inválidos |
| 500 | Internal Server Error | Erro no código do servidor |

---

## Seção 7 — Pydantic e schemas (schemas.py)

### O que é Pydantic

Pydantic é um validador. Quando alguém faz POST na API, o Pydantic verifica
se os dados vieram corretos antes de qualquer coisa. Se faltar um campo
obrigatório, ele retorna um erro 422 automaticamente — sem você precisar
escrever nenhuma validação manual.

### Por que há schemas separados do model do banco

O banco tem campos que o servidor gera automaticamente (`id`, `criada_em`).
O usuário não manda esses campos no POST — ele manda só os dados da rota.

Por isso existem 3 schemas diferentes:

| Schema | Quando é usado | Tem `id`? | Tem `criada_em`? |
|--------|---------------|:---------:|:---------------:|
| `RotaCreate` | POST — o que o usuário manda | Não | Não |
| `RotaUpdate` | PUT — o que pode ser atualizado | Não | Não |
| `RotaResponse` | Toda resposta da API | Sim | Sim |

### O que os meninos preenchem em schemas.py

O `RotaCreate` e o `RotaUpdate`. O `RotaResponse` já está pronto.

Exemplo do que `RotaCreate` deve ficar:
```python
class RotaCreate(BaseModel):
    nome: str
    escola_destino: str
    horario_saida: str
    horario_retorno: str
    descricao: Optional[str] = None
```

### IMPORTANTE: .model_dump() não .dict()

No Pydantic v2, o método para converter em dicionário é `.model_dump()`.
O `.dict()` era da versão 1 e está obsoleto.
Se um menino usar `.dict()`, significa que copiou de um tutorial antigo
sem entender o que estava fazendo.

---

## Seção 8 — SQLAlchemy (models.py e database.py)

### O que é um ORM

ORM = Object Relational Mapper.
É um tradutor entre Python e SQL.

Sem ORM você escreveria:
```sql
SELECT * FROM rotas_transporte WHERE ativa = 1
```

Com SQLAlchemy você escreve Python:
```python
db.query(RotaTransporte).filter(RotaTransporte.ativa == True).all()
```

O SQLAlchemy traduz isso para SQL automaticamente.

### O que é uma Session

A Session é a "conversa ativa" com o banco de dados.
Pense como uma transação: você faz mudanças, e só quando chama `db.commit()`
as mudanças são salvas de verdade.

| Operação | O que faz |
|----------|-----------|
| `db.query(Model).all()` | Busca todos os registros |
| `db.query(Model).filter(...).all()` | Busca com condição |
| `db.get(Model, id)` | Busca por ID — retorna None se não existe |
| `db.add(objeto)` | Prepara o objeto para ser salvo |
| `db.commit()` | Confirma e salva no banco |
| `db.refresh(objeto)` | Atualiza o objeto com dados do banco (pega o id gerado) |

### Por que db.refresh() é importante

Depois de `db.commit()`, o SQLAlchemy "esquece" os dados do objeto (performance).
Se você tentar retornar o objeto sem `db.refresh()`, vai receber um erro críptico
de serialização. O `db.refresh()` recarrega os dados do banco para o objeto.

No template, o `db.refresh()` já está pré-scaffolado nos endpoints de POST e PUT.
Os meninos não precisam saber disso — mas é importante você entender.

### O que é SQLite (por que não precisa instalar nada)

O SQLite é um banco de dados que vive em um único arquivo no seu projeto.
Diferente do PostgreSQL (que tem um servidor separado), o SQLite não precisa
de instalação — já vem com o Python.

Para este desafio, usamos SQLite porque:
- Zero configuração
- Funciona em qualquer máquina
- Foco no que importa: código da API

No projeto real, usaremos PostgreSQL — mas o código da API em si muda muito pouco.

---

## Seção 9 — Os 5 endpoints e o que eles fazem (rotas.py)

### O que já está pronto no scaffold

- Assinatura de cada função (nome, parâmetros, decorators)
- `response_model` (tipo de retorno)
- `status_code=201` no POST
- `db.refresh(rota)` nos endpoints de POST e PUT
- Dicas detalhadas nos comentários de cada TODO

### A solução esperada de cada endpoint

**GET /rotas/ — listar rotas ativas:**
```python
return db.query(RotaTransporte).filter(RotaTransporte.ativa == True).all()
```

**GET /rotas/{id} — buscar por ID:**
```python
rota = db.get(RotaTransporte, id)
if not rota or not rota.ativa:
    raise HTTPException(status_code=404, detail="Rota não encontrada")
return rota
```

**POST /rotas/ — criar:**
```python
rota = RotaTransporte(**dados.model_dump())
db.add(rota)
db.commit()
# db.refresh(rota) já está no scaffold
return rota
```

**PUT /rotas/{id} — atualizar:**
```python
rota = db.get(RotaTransporte, id)
if not rota or not rota.ativa:
    raise HTTPException(status_code=404, detail="Rota não encontrada")
for campo, valor in dados.model_dump(exclude_unset=True).items():
    setattr(rota, campo, valor)
db.commit()
# db.refresh(rota) já está no scaffold
return rota
```

**DELETE /rotas/{id} — soft delete:**
```python
rota = db.get(RotaTransporte, id)
if not rota or not rota.ativa:
    raise HTTPException(status_code=404, detail="Rota não encontrada")
rota.ativa = False
db.commit()
return {"ok": True}
```

---

## Seção 10 — Pytest e testes (test_rotas.py)

### O que é um teste automatizado

É uma função Python que verifica automaticamente se o código funciona.
Cada `assert` é uma verificação. Se o assert falhar, o teste falha e mostra
exatamente qual linha e qual valor era esperado vs o que veio.

### Como rodar

```
pytest -v
```

O `-v` (verbose) mostra o nome de cada teste:
```
tests/test_rotas.py::test_criar_rota PASSED        [33%]
tests/test_rotas.py::test_rota_nao_encontrada PASSED [66%]
tests/test_rotas.py::test_deletar_rota PASSED      [100%]
```

### O que é a fixture client (conftest.py)

A fixture `client` configura:
1. Um banco de dados **em memória** (não cria arquivo, não polui o dev)
2. Um TestClient — cliente HTTP falso que simula requisições reais
3. Limpeza automática ao final de cada teste

Os meninos usam assim:
```python
def test_criar_rota(client):  # ← "client" é injetado automaticamente
    response = client.post("/rotas/", json={...})
```

### O que os meninos completam

Os asserts dos 3 testes. A solução esperada:

**test_criar_rota:**
```python
assert response.status_code == 201
assert response.json()["nome"] == DADOS_ROTA["nome"]
assert response.json()["ativa"] == True
assert "id" in response.json()
```

**test_rota_nao_encontrada:**
```python
assert response.status_code == 404
```

**test_deletar_rota:**
```python
delete_response = client.delete(f"/rotas/{id_criado}")
assert delete_response.status_code == 200

get_response = client.get(f"/rotas/{id_criado}")
assert get_response.status_code == 404
```

---

## Seção 11 — Ruff e Black

### Ruff — linter

Detecta problemas no código **sem precisar executar**.

```
ruff check .
```

Exemplos do que encontra:
- `F401` — import não utilizado
- `F841` — variável criada mas nunca usada
- `E711` — comparação errada com None (`== None` ao invés de `is None`)

### Black — formatter

Reformata o código automaticamente para um padrão consistente.

```
black .
```

Só para verificar sem alterar:
```
black --check .
```

Por que isso importa: em time, todo mundo formata diferente. O Black elimina
discussões sobre estilo e mantém o diff dos PRs limpo (só mudanças de lógica,
não de espaçamento).

---

## Seção 12 — Git workflow do desafio

### O que os meninos fazem

1. **Fork** — botão "Fork" na página do seu repo no GitHub. Cria uma cópia
   do repo na conta deles.

2. **Clone** — baixa o fork para a máquina local:
   ```
   git clone https://github.com/nome-deles/pjapp-desafio-template.git
   ```

3. **Branch** — cria uma branch com o nome deles:
   ```
   git checkout -b feat/vitor-crud-rotas
   ```

4. **Commitar** ao longo do desenvolvimento:
   ```
   git add .
   git commit -m "feat: implementar schemas RotaCreate e RotaUpdate"
   git commit -m "feat: implementar endpoints GET /rotas e GET /rotas/{id}"
   git commit -m "test: completar asserts do test_criar_rota"
   ```

5. **Push e PR**:
   ```
   git push origin feat/vitor-crud-rotas
   ```
   Depois abrir o PR no GitHub.

### O que você observa no histórico

Acesse o PR deles e clique em "Commits". Você vai ver:
- Quantos commits fizeram e quando (ritmo de trabalho)
- Se commitaram tudo de uma vez (provável que deixaram para o final) ou ao longo do desenvolvimento
- Se as mensagens de commit descrevem o que foi feito ou são genéricas ("update", "fix")

---

## Seção 13 — Publicar o template no GitHub

### Passo a passo

1. Garantir que todos os arquivos estão na pasta `pjapp-desafio-template/`

2. Abrir o terminal **na pasta do template**:
   ```
   cd C:\Users\Guilherme\Desktop\IA\pjapp-desafio-template
   ```

3. Inicializar o Git:
   ```
   git init
   git add .
   git commit -m "feat: template inicial do desafio"
   ```

4. Criar o repo no GitHub:
   - Acessar [github.com](https://github.com) → botão "New"
   - Nome: `pjapp-desafio-template`
   - Visibilidade: **Public** (os meninos precisam fazer fork)
   - **Não marcar** "Initialize with README" (já temos)
   - Clicar "Create repository"

5. Conectar e fazer push:
   ```
   git branch -M main
   git remote add origin https://github.com/guibsoliveira/pjapp-desafio-template.git
   git push -u origin main
   ```

6. Marcar como template (opcional mas recomendado):
   - No repo no GitHub → Settings → marcar "Template repository"
   - Isso cria um botão "Use this template" na página do repo

### Como os meninos fazem fork

Na página do repo no GitHub, clicar no botão **Fork** (canto superior direito).
Isso cria uma cópia do repo na conta deles. Eles trabalham na cópia deles
e abrem um PR apontando para o seu repo.

---

## Seção 14 — O que observar na avaliação técnica

### No código deles

| O que ver | Sinal positivo | Sinal de alerta |
|-----------|---------------|-----------------|
| `.model_dump()` vs `.dict()` | Usou `.model_dump()` | Usou `.dict()` = copiou tutorial antigo |
| 404 no GET e DELETE | Verificou em ambos | Verificou só em um |
| Soft delete | `rota.ativa = False` | `db.delete(rota)` = não entendeu a spec |
| Asserts dos testes | Verifica campos específicos | Só verifica `status_code == 200` |
| Commits | Vários commits ao longo do tempo | Um commit gigante no final |

### Perguntas para a apresentação de 15 minutos

Faça estas perguntas para testar entendimento real vs decoreba:

- *"Por que o `db.refresh()` está depois do `db.commit()`?"*
  → Resposta esperada: "Para recarregar o objeto com o id e criada_em gerados"

- *"O que acontece se alguém fizer DELETE e depois GET na mesma rota?"*
  → Resposta esperada: "O GET retorna 404 porque a rota está inativa"

- *"Qual a diferença entre `schemas.py` e `models.py`?"*
  → Resposta esperada: "models é a estrutura do banco, schemas é o que a API recebe/retorna"

- *"Por que o teste usa um banco separado e não o banco real?"*
  → Resposta esperada: "Para não poluir os dados reais e garantir isolamento"

- *"O que o `exclude_unset=True` faz no PUT?"*
  → Resposta esperada: "Atualiza só os campos que o usuário enviou, não todos"

---

## Verificação antes de mandar para os meninos

Execute todos estes comandos em sequência e confirme os resultados:

```bash
# 1. Python
python --version
# Esperado: Python 3.11.x ou superior

# 2. Criar e ativar venv
python -m venv venv
.\venv\Scripts\Activate.ps1
# Esperado: (venv) aparece no terminal

# 3. Instalar dependências
pip install -r requirements.txt
# Esperado: instalação sem erros

# 4. Subir a API
uvicorn app.main:app --reload
# Esperado: "Uvicorn running on http://127.0.0.1:8000"
# Abrir http://127.0.0.1:8000/docs — deve mostrar 5 endpoints + /health

# 5. Rodar testes (em outro terminal com venv ativado)
pytest -v
# Esperado: 3 testes FALHANDO — isso é CORRETO
# O template tem TODOs vazios propositalmente
# FAILED tests/test_rotas.py::test_criar_rota
# FAILED tests/test_rotas.py::test_rota_nao_encontrada
# FAILED tests/test_rotas.py::test_deletar_rota

# 6. Linter
ruff check .
# Esperado: sem erros nos arquivos fornecidos

# 7. Formatter
black --check .
# Esperado: "All done! ✨ 🍰 ✨"
```

**Se todos estes passos passarem → o template está pronto para os meninos.**
