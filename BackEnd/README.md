# Backend

API do projeto de futebol, desenvolvida com FastAPI. Esta documentação descreve o papel previsto para os arquivos principais do backend; os módulos ainda estão em construção.

## Estrutura e responsabilidades

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Ponto de entrada da API. Deve criar a aplicação FastAPI, configurar itens gerais (como metadados e middleware, quando necessários) e registrar os routers para disponibilizar suas rotas. |
| `core/config.py` | Reunir configurações usadas em diferentes partes da aplicação, lendo valores do ambiente e fornecendo padrões apropriados para desenvolvimento. Isso evita espalhar configurações pelo código. |
| `routers/clubes.py` | Declarar as rotas HTTP relacionadas a clubes, receber parâmetros e dados da requisição, chamar a camada de serviço e devolver respostas com os códigos HTTP adequados. |
| `schemas/clube.py` | Definir modelos Pydantic para validar e serializar os dados de clube recebidos e enviados pela API. Os schemas também podem diferenciar dados de criação, atualização e resposta. |
| `services/clube_service.py` | Concentrar as regras de negócio de clubes, como criação, consulta, alteração e remoção, além de coordenar o acesso aos dados e tratar situações como clube inexistente ou duplicado. |
| `requirements.txt` | Listar as dependências Python necessárias ao backend, com versões fixadas para tornar a instalação do ambiente reproduzível. Instale-as com `pip install -r requirements.txt`. |
| `.env` | Guardar valores locais de configuração, como URLs e credenciais, que podem variar entre ambientes. O arquivo deve permanecer privado; use um `.env.example` sem segredos para documentar as variáveis necessárias. |
| `.gitignore` | Indicar ao Git arquivos e diretórios locais que não devem ser versionados, por exemplo `.env`, `.venv/`, `__pycache__/` e arquivos de cache. |

## Ambiente de desenvolvimento

No Windows, a partir da pasta `BackEnd`, crie e ative um ambiente virtual e instale as dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Quando `main.py` estiver implementado como ponto de entrada ASGI, a API poderá ser iniciada em modo de desenvolvimento com:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8001
```

Esse comando pressupõe que `main.py` exponha uma variável chamada `app`. A interface interativa do FastAPI fica normalmente disponível em `/docs` enquanto o servidor estiver em execução.
