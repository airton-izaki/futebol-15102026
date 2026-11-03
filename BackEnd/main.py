
from fastapi                import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib             import asynccontextmanager
from core.database          import Base, engine

import models.clube
import models.campeonato
import models.rodada
import models.jogo
import routers.localidades

from routers                import clube, localidades, campeonato_router, jogo_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title = "API do Campeonato de Futebol",
    description = "API para gerenciamento de clubes e acompanhamento do campeonato.",
    lifespan = lifespan,
    version = "1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clube.router)
app.include_router(localidades.router)
app.include_router(campeonato_router.router)
app.include_router(jogo_router.router)


@app.get("/")
def inicio():
    return {"mensagem": "API do Campeonato de Futebol está ativa."}
