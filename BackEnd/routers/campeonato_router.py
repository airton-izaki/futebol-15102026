from fastapi                        import APIRouter, Depends, status
from sqlalchemy.orm                 import Session
from typing                         import List

from schemas.campeonato_shcema      import CampeonatoCreate, CampeonatoResponse
from services.campeonato_service    import cadastrar_campeonato
from core.database                  import get_db


router = APIRouter(
    prefix = "/campeonatos",
    tags = ["Campeonatos"],
)

@router.post(
    response_model = CampeonatoResponse,
    status_code = status.HTTP_201_CREATED,
    summary = "Cadastrar um novo campeonato",
)

async def criar_campeonato(
    campeonato_data: CampeonatoCreate,
    db: Session = Depends(get_db),
):
    """
    Recebe os dados validados do Angular, aplica as regras de negócio
    no service e persiste o campeonato no banco de dados.
    """
    campeonato_criado = await cadastrar_campeonato(db = db, campeonato_data=campeonato_data)

    return campeonato_criado

