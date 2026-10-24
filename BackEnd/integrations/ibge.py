import httpx

from core.config    import IBGE_API_URL

async def consultar_estados():
    url = f"{IBGE_API_URL}/estados"

    async with httpx.AsyncClient(timeout = 15.0) as client:
        resposta = await client.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

    return [
        {
            "id": estado["id"],
            "sigla": estado["sigla"],
            "nome": estado["nome"],
        }
        for estado in dados
    ]


async def consultar_municipios(uf_id: int):
    url = f"{IBGE_API_URL}/estados/{uf_id}/municipios"

    async with httpx.AsyncClient(timeout = 15.0) as client:
        resposta = await client.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

    return [
        {
            "id": municipio["id"],
            "nome": municipio["nome"],
        }
        for municipio in dados
    ]










