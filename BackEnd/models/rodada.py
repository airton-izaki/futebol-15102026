from sqlalchemy         import Boolean , ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm     import Mapped, mapped_column
from core.database      import Base


class Rodada(Base):
    __tablename__ = "rodada"

    __table_args__ = (                      # Garante que não exista duas "1ª Rodadas" para o mesmo campeonato                                    
        UniqueConstraint(
            'campeonato_id', 'numero', 
            name = 'uq_campeonato_rodada'
        ),
    )

    id: Mapped[int] = mapped_column(
            primary_key = True,
            index = True,    
    )

    campeonato_id: Mapped[int] = mapped_column(
        ForeignKey("campeonato.id"),
        nullable = False
    )

    numero: Mapped[int] = mapped_column(
        Integer,
        nullable = False,
        comment = "Ex: 1 para 1ª Rodada"
    )

    ativa: Mapped[bool] = mapped_column(
        Boolean,
        nullable = False,
        default = False
    )