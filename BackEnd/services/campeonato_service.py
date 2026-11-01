from fastapi                    import HTTPException, status
from sqlalchemy.orm             import Session
from models.campeonato          import Campeonato
from schemas.campeonato_shcema  import CampeonatoCreate


async def cadastrar_campeonato(db: Session, campeonato_data: CampeonatoCreate) -> Campeonato:
    """
    Regra de negócio para cadastrar um novo campeonato.
    Verifica duplicidade e persiste no banco de dados.
    """

    # 1. Regra de Negócio: Verificar se já existe um campeonato igual na mesma temporada
    campeonato_existente = db.query(Campeonato).filter(
        Campeonato.nome_campeonato == campeonato_data.nome_campeonato,
        Campeonato.temporada == campeonato_data.temporada
    ).first()

    if campeonato_existente:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Já existe um campeonato com este nome cadastrado para esta temporada."
        )

    # 2. Criando a instância do Model do SQLAlchemy com os dados limpos do Schema
    novo_campeonato = Campeonato(
        nome_campeonato = campeonato_data.nome_campeonato,
        temporada = campeonato_data.temporada
    )

    # 3. Persistindo no Banco de Dados
    db.add(novo_campeonato)
    db.commit()
    db.refresh(novo_campeonato)  # Atualiza o objeto para trazer o ID gerado e as datas do banco

    return novo_campeonato

