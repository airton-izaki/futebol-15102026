from fastapi                import HTTPException, status
from typing                 import List
from sqlalchemy.orm         import Session, joinedload
from models.jogo            import Jogo
from schemas.jogo_schema    import JogoCreate, JogoUpdate


async def _verificar_time_ja_joga_na_rodada(db: Session, rodada_id: int, time_id: str, jogo_id_atual: int = None):
    """Verifica se o time já possui um jogo cadastrado nesta mesma rodada."""
    query = db.query(Jogo).filter(
        Jogo.rodada_id == rodada_id,
        (Jogo.time_mandante_id == time_id) | (Jogo.time_visitante_id == time_id)
    )

    if jogo_id_atual:
        query = query.filter(Jogo.id != jogo_id_atual)

    return query.first() is not None

async def obter_jogo(db: Session, jogo_id: int) -> Jogo:

    """Busca um jogo específico pelo ID carregando seus relacionamentos."""
    jogo = (
        db.query(Jogo).options(
            joinedload(Jogo.campeonato),
            joinedload(Jogo.rodada),
            joinedload(Jogo.time_mandante),
            joinedload(Jogo.time_visitante),
            joinedload(Jogo.sumula),
        ).filter(Jogo.id == jogo_id).filter()
    )

    if jogo is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Jogo não encontrado"
        )

    return jogo

async def cadastrar_jogo(db: Session, jogo_data: JogoCreate) -> Jogo:
    """Cadastra um novo jogo após validar os dados básicos."""
    
    # Regra: Time mandante e visitante não podem ser o mesmo
    if jogo_data.time_mandante_id == jogo_data.time_visitante_id:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "O time mandante e o time visitante não podem ser o mesmo."
        )

    # 2. Regra: Um time só pode jogar uma vez por rodada
    if await _verificar_time_ja_joga_na_rodada(db, jogo_data.rodada_id, jogo_data.time_mandante_id):
        clube = db.query(clube).filter(clube.id == jogo_data.time_mandante_id).first()
        nome_time = clube.nome if clube else jogo_data.time_mandante_id
        
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"O time {nome_time} já possui um jogo agendado nesta rodada."
        )

    if await _verificar_time_ja_joga_na_rodada(db, jogo_data.rodada_id, jogo_data.time_visitante_id):
        clube = db.query(clube).filter(clube.id == jogo_data.time_visitante_id).first()
        nome_time = clube.nome if clube else jogo_data.time_visitante_id

        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"O time {nome_time} já possui um jogo agendado nesta rodada."
        )

    # 3. Criação do Jogo
    novo_jogo = Jogo(
        campeonato_id = jogo_data.campeonato_id,
        rodada_id = jogo_data.rodada_id,
        time_mandante_id = jogo_data.time_mandante_id,
        time_visitante_id = jogo_data.time_visitante_id,
        local = jogo_data.local,
        data_jogo = jogo_data.data_jogo,
        hora_jogo = jogo_data.hora_jogo,
        observacao = jogo_data.observacao,
    )

    try:
        db.add(novo_jogo)
        db.commit()
        db.refresh(novo_jogo)

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"Erro ao persistir o jogo no banco de dados: {str(e)}"
        )

    return await obter_jogo(db, novo_jogo.id)


async def listar_jogos(db: Session) -> List[Jogo]:
    try:
        return(
            db.query(Jogo).options(
                joinedload(Jogo.campeonato),
                joinedload(Jogo.rodada),
                joinedload(Jogo.time_mandante),
                joinedload(Jogo.time_visitante),
                joinedload(Jogo.sumula),

            ).all()
        )

    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"Erro ao buscar jogos na base de dados: {str(e)}",
        )

async def atualizar_jogo(db: Session, jogo_id: int, jogo_data: JogoUpdate) -> Jogo:
    jogo = await obter_jogo(db, jogo_id)

    mandante_id = jogo_data.time_mandante_id   if jogo_data.time_mandante_id is not None else jogo.time_mandante_id
    visitante_id = jogo_data.time_visitante_id if jogo_data.time_mandante_id is not None else jogo.time_visitante_id
    rodada_id = jogo_data.rodada_id if jogo_data.rodada_id is not None else jogo.rodada_id

    if mandante_id == visitante_id:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "O time mandante e o time visitante não podem ser o mesmo."
        )

    if await _verificar_time_ja_joga_na_rodada(db, rodada_id, mandante_id, jogo_id_atual = jogo.id):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "O time mandante já possui outro jogo agendado nesta rodada."
        )

    if await _verificar_time_ja_joga_na_rodada(db, rodada_id, visitante_id, jogo_id_atual = jogo.id):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "O time visitante já possui outro jogo agendado nesta rodada."
        )

    dados_atualizacao = jogo_data.model_dump(exclude_unset = True)
    for chave, valor in dados_atualizacao.items():
        setattr(jogo, chave, valor)

    try:
        db.commit()
        db.refresh(jogo)

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"Erro ao atualizar o jogo no banco de dados: {str(e)}"
        )

    return await obter_jogo(db, jogo.id)

    