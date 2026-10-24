
from fastapi                import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib             import asynccontextmanager
from core.database          import Base, engine
from routers                import clube, localidades
from models                 import clube as clube_model

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



@app.get("/")
def inicio():
    return {"mensagem": "API do Campeonato de Futebol está ativa."}
