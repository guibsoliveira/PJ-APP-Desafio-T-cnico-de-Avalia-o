# PJ-APP — Desafio Técnico de Avaliação

Bem-vindo ao desafio técnico do PJ-APP.

Este repositório é um template de um projeto Python com FastAPI. Sua missão é implementar uma API de **CRUD de Rotas de Transporte Escolar**.

---

## O que você vai construir

Uma API REST com 5 endpoints para gerenciar rotas de transporte escolar.

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/rotas/` | Lista todas as rotas ativas |
| GET | `/rotas/{id}` | Busca uma rota pelo ID |
| POST | `/rotas/` | Cria uma nova rota |
| PUT | `/rotas/{id}` | Atualiza uma rota existente |
| DELETE | `/rotas/{id}` | Desativa uma rota (sem apagar do banco) |

---

## Modelo de dados — Rota de Transporte

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|:-----------:|-----------|
| `id` | inteiro | auto | Gerado automaticamente |
| `nome` | texto | sim | Nome da rota |
| `escola_destino` | texto | sim | Escola de destino |
| `horario_saida` | texto | sim | Formato: "07:30" |
| `horario_retorno` | texto | sim | Formato: "17:30" |
| `descricao` | texto | não | Descrição opcional |
| `ativa` | booleano | auto | True por padrão |
| `criada_em` | data/hora | auto | Gerado automaticamente |

---

## O que já está pronto (não modifique)

- `app/main.py` — configuração da API
- `app/database.py` — conexão com o banco de dados
- `app/models.py` — estrutura da tabela no banco
- `app/schemas.py` — schema de resposta (`RotaResponse`)
- `tests/conftest.py` — setup dos testes

## O que você precisa implementar

- `app/schemas.py` — schemas `RotaCreate` e `RotaUpdate` (campos de entrada)
- `app/routers/rotas.py` — lógica dos 5 endpoints
- `tests/test_rotas.py` — asserts dos 3 testes

---

## Como configurar o ambiente

### 1. Verificar Python

Abra o terminal no VS Code (`Ctrl + \``) e execute:

```
python --version
```

Deve mostrar `Python 3.11.x` ou superior. Se não tiver Python instalado, baixe em [python.org](https://python.org/downloads) e **marque "Add Python to PATH"** durante a instalação.

### 2. Criar o ambiente virtual

```
python -m venv venv
```

### 3. Ativar o ambiente virtual

**PowerShell:**
```
.\venv\Scripts\Activate.ps1
```

**CMD (Prompt de Comando):**
```
venv\Scripts\activate.bat
```

> Se o PowerShell der erro de permissão, execute uma vez:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
> Depois ative novamente.

Quando ativado, o terminal mostrará `(venv)` no início.

### 4. Instalar as dependências

```
pip install -r requirements.txt
```

### 5. Subir a API

```
uvicorn app.main:app --reload
```

Acesse `http://127.0.0.1:8000/docs` para ver a documentação interativa da API.

### 6. Rodar os testes

```
pytest -v
```

Os 3 testes devem estar **falhando** antes de você implementar — isso é esperado.
Ao terminar, todos os 3 devem estar **passando**.

---

## Git — fluxo esperado

1. Faça **fork** deste repositório no GitHub
2. Clone o fork para sua máquina: `git clone URL_DO_SEU_FORK`
3. Crie uma branch: `git checkout -b feat/seu-nome-crud-rotas`
4. Implemente as funcionalidades e faça commits ao longo do processo
5. Use **conventional commits**: `feat:`, `fix:`, `test:`, `docs:`
   - Exemplo: `git commit -m "feat: implementar endpoint GET /rotas"`
6. Faça push: `git push origin feat/seu-nome-crud-rotas`
7. Abra um **Pull Request** no GitHub com uma boa descrição

---

## Critérios de avaliação

| Critério | Peso |
|----------|:----:|
| Comprometimento (checkpoints no prazo) | 15% |
| Comunicação (PR description, apresentação) | 10% |
| Autonomia (buscou documentação, não ficou parado) | 15% |
| Lógica de programação (código correto e organizado) | 15% |
| Organização (commits, branch, README) | 10% |
| Git e GitHub (uso correto do fluxo) | 10% |
| API funcionando (endpoints corretos) | 10% |
| Testes (3 testes passando) | 5% |
| Leitura de documentação (seguiu a spec) | 5% |
| Capacidade de aprender (evolução visível) | 5% |

**Nota mínima para aprovação: 6.0/10**

---

## Prazo

7 dias corridos a partir do recebimento deste desafio.

**Checkpoints obrigatórios:**
- **Dia 2:** branch criada + pelo menos 2 commits feitos
- **Dia 5:** API funcionando localmente (ao menos 3 endpoints)
- **Dia 7:** PR aberto + apresentação de 15 minutos

---

## Apresentação (15 minutos)

Na apresentação você vai explicar:

1. O que é Git e GitHub e como usou no desafio
2. O que você construiu e como funciona
3. Decisões que tomou e por quê
4. Dificuldades que encontrou e como resolveu

---

## Dúvidas

Se travar em algo de ambiente ou configuração, avise. Se travar em lógica de programação, tente resolver sozinho primeiro — pesquise a documentação do FastAPI em [fastapi.tiangolo.com](https://fastapi.tiangolo.com). A capacidade de buscar e entender documentação é parte do que será avaliado.
