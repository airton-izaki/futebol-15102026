from fastapi                import APIRouter, Depends, status
from sqlalchemy.orm         import Session
from typing                 import List
from core.database          import get_db

from schemas.jogo_schema    import JogoCreate, JogoUpdate, JogoDetailResponse
from services               import jogo_service



router = APIRouter( prefix = "/jogos",  tags = ["jogos"] )

@router.post(
    "/",
    response_model = JogoDetailResponse,
    status_code = status.HTTP_201_CREATED
)
async def cadastrar_jogo(jogo_data: JogoCreate, db: Session = Depends(get_db)):
    """Cadastra um novo jogo validando as regras da rodada."""
    return await jogo_service.cadastrar_jogo(db, jogo_data)

@router.get(
    "/",
    response_model = List[(JogoDetailResponse)]
)
async def listar_jogos(db:Session = Depends(get_db)):
    """Lista todos os jogos cadastrados com dados detalhados (clubes, campeonato, rodada e súmula)."""
    return await jogo_service.listar_jogos(db)

@router.get(
    "/{jogo_id}",
    response_model = JogoDetailResponse
)
async def obter_jogo(jogo_id: int, db:Session = Depends(get_db)):
    """Busca os detalhes de um jogo específico pelo ID."""
    return await jogo_service.obter_jogo(db, jogo_id)

@router.post(
    "/{jogo_id}",
    response_model = JogoDetailResponse
)
async def atualizar_jogo(jogo_id: int, jogo_data:JogoUpdate, db:Session = Depends(get_db)):
    """Atualiza os dados de um jogo existente."""
    return await jogo_service.atualizar_jogo(db, jogo_id, jogo_data)




