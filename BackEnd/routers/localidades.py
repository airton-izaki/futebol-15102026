import httpx

from fastapi            import APIRouter, HTTPException
from integrations.ibge  import consultar_estados, consultar_municipios


router = APIRouter(
    prefix = "/localidades",
    tags = ["Localidades"],
)

@router.get("/estados")
async def listar_estados():
    try:
        return await consultar_estados()

    except httpx.HTTPError:
        raise HTTPException(
            status_code = 502,
            detail = "Não foi possível consultar os estados no IBGE.",
        )

@router.get("/estados/{uf_id}/municipios")
async def listar_municipios(uf_id: int):
    try:
        return await consultar_municipios(uf_id)
    
    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Não foi possível consultar os municípios no IBGE.",
        )

