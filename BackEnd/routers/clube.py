from fastapi                import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm         import Session
from typing                 import List

from schemas.clube          import ClubeCreate, ClubeResponse
from services.clube_service import cadastrar_clube, Listar_Clube, obter_clube, atualizar_clube
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


@router.get(
    "/",
    response_model = List[ClubeResponse],
    summary = "Listar todos os clubes cadastrados",
)

async def Listar_Clubes(db: Session = Depends(get_db)):
    """Retorna a lista completa de clubes registados com os respetivos dados e localidades."""
    return await Listar_Clube(db = db)


@router.get("/{clube_id}", response_model=ClubeResponse, summary="Consultar um clube")
async def consultar_clube(clube_id: int, db: Session = Depends(get_db)):
    return await obter_clube(db=db, clube_id=clube_id)


@router.put("/{clube_id}", response_model=ClubeResponse, summary="Atualizar um clube")
async def editar_clube(clube_id: int, clube_data: ClubeCreate, db: Session = Depends(get_db)):
    return await atualizar_clube(db=db, clube_id=clube_id, clube_data=clube_data)



