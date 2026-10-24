from fastapi            import HTTPException, status
from sqlalchemy.orm     import Session

from models.clube       import Clube
from schemas.clube      import ClubeCreate
from integrations.ibge  import consultar_dados_municipio

"""Coordena as regras de negócio para o cadastro de um novo clube:

    1. Valida e obtém dados oficiais da localidade via IBGE usando o código informado.
    2. Combina os dados do Pydantic com o retorno do IBGE.
    3. Instancia e persiste o modelo SQLAlchemy no banco de dados.
    4. Retorna o objeto persistido.

"""
async def cadastrar_clube(db: Session, clube_data: ClubeCreate) -> Clube:

    # 1. Consultar e validar dados do município pelo código IBGE enviado pelo Angular
    try:
        localizacao = await consultar_dados_municipio(clube_data.codigo_ibge_municipio)

    except Exception as e:
        # Se o IBGE retornar 404 ou falhar, tratamos como erro de validação/serviço
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Não foi possível validar o código IBGE informado. Detalhe: {str(e)}",
        )

    # 2. Criar a instância do modelo SQLAlchemy com os dados validados
    novo_clube = Clube(
        nome_oficial = clube_data.nome_oficial,
        nome = clube_data.nome,
        sigla = clube_data.sigla,
        gestao = clube_data.gestao.name,
        fundacao = clube_data.fundacao,
        codigo_ibge_municipio = clube_data.codigo_ibge_municipio,
        cidade = localizacao["nome"],
        estado_nome = localizacao["estado_nome"],
        estado_sigla = localizacao["estado_sigla"],
        estadio = clube_data.estadio,
        cor_primaria = clube_data.cor_principal,
        cor_secundaria = clube_data.cor_secundaria,
        cor_terciaria = clube_data.cor_terciaria,
        website = str(clube_data.website) if clube_data.website else None,
        escudo = str(clube_data.escudo) if clube_data.escudo else None,
        descricao = clube_data.descricao,
        ativo = clube_data.ativo,
    )

    # 3. Salvar o registro no banco de dados
    try:
        db.add(novo_clube)
        db.commit()
        db.refresh(novo_clube)

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"Erro ao persistir o clube no banco de dados: {str(e)}",
        )

    # 4. Devolver o clube cadastrado para o Router responder ao Angular
    return novo_clube

















