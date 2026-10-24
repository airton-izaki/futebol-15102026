
from fastapi import FastAPI
from routers.localidades    import router as localidades_router


app = FastAPI(
    title = "API do Campeonato de Futebol",
    description = "API para gerenciamento de clubes e acompanhamento do campeonato.",
    version = "1.0.0",
)

app.include_router(localidades_router)

@app.get("/")
def inicio():
    return {"mensagem": "API do Campeonato de Futebol está ativa."}