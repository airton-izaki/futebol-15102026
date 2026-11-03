from datetime import date, time
from sqlalchemy import Boolean, Date, ForeignKey, Integer, String, Text, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base


class Jogo(Base):
    __tablename__ = "jogo"


    id: Mapped[int] = mapped_column(
            primary_key = True,
            index = True,    
    )

    campeonato_id: Mapped[int] = mapped_column(
        ForeignKey("campeonato.id"), 
        nullable = False
    )

    rodada_id: Mapped[int] = mapped_column(
        ForeignKey("rodada.id"), 
        nullable = False
    )

    time_mandante_id: Mapped[str] = mapped_column(
        ForeignKey("clube.id"), 
        nullable = False
    )

    time_visitante_id: Mapped[str] = mapped_column(
        ForeignKey("clube.id"), 
        nullable = False
    )

    local: Mapped[str] = mapped_column(
        String(150), 
        nullable = True, 
        comment = "Estádio do jogo"
    )

    data_jogo: Mapped[date] = mapped_column(
        Date,
        nullable = False
    )


    hora_jogo: Mapped[time] = mapped_column(
        Time,
        nullable = False,
    )


    observacao: Mapped[str] = mapped_column(
        Text, 
        nullable = True,
        comment = "Observações sobre o agendamento (remarcação, mudança de local, portões fechados, etc."
    )

    # Relacionamentos
    campeonato = relationship(
        "campeonato",
        back_populates = "Jogos"
    )

    rodada = relationship(
        "Rodada",
        back_populates = "Jogos"
    )

    time_mandante = relationship(
        "clube",
        foreign_keys = [time_mandante_id]
    )

    time_visitante = relationship(
        "clube",
        foreign_keys = [time_visitante_id]
    )

    sumula = relationship(
        "Sumula",
        back_populates = "jogo",
        uselist = False,
        cascade = "all, delete-orphan"
    )
