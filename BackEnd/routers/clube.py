from fastapi                import APIRouter, Depends, status
from sqlalchemy.orm         import Session

from schemas.clube          import ClubeCreate, ClubeResponse
from services.clube_service import cadastrar_clube
from core.database          import get_db

router = APIRouter(
    prefix = "/clubes",
    tags = ["Clubes"],
)

@router.post(
    "/",
    response_model = ClubeResponse,
    status_code = status.HTTP_201_CREATED,
    summary = "Cadastrar um novo clube",
)

async def criar_clube(
    clube_data: ClubeCreate,
    db: Session = Depends(get_db),
):

    """Recebe os dados validados do Angular, valida o código IBGE,
        associa a localidade e persiste o clube no banco de dados.
    """
    clube_criado = await cadastrar_clube(db=db, clube_data=clube_data)

    return clube_criado













