from datetime           import date, datetime
from sqlalchemy         import Boolean, CheckConstraint, Date, DateTime, Integer, String, Text, func, true
from sqlalchemy.orm     import Mapped, mapped_column
from core.database      import Base


class Clube(Base):
    __tablename__ = "Clube"                 #  Define o nome da tabela que será criada no

    __table_args__ = (
        CheckConstraint(
            "gestao IN ('ASSOCIATIVO', 'SAF', 'PRIVADO', 'HIBRIDO')",
            name = "ck_clube_gestao",
        )
    )

    id: Mapped[int] = mapped_column(
        primary_key = True,
        index = True,
    )
    nome_oficial: Mapped[str] = mapped_column(
        String(100),
        nullable = False,
    )
    nome: Mapped[str] = mapped_column(
        String(50),
        nullable = False,
    )
    sigla: Mapped[str] = mapped_column(
        String(5),
        nullable = False,
    )
    gestao: Mapped[str] = mapped_column(
        String(20),
        nullable = False,
        Default = "ASSOCIATIVO",
    )
    fundacao: Mapped[date] = mapped_column(
        Date,
        nullable = False,
    )
    codigo_ibge_municipio: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    cidade: Mapped[str] = mapped_column(
        String(100),
        nullable = False,
    )
    estado_nome: Mapped[str] = mapped_column(
        String(100),
        nullable = False,
    )
    estado_sigla: Mapped[str] = mapped_column(
        String(2),
        nullable = False,
    )
    estadio: Mapped[str] = mapped_column(
        String(100),
        nullable = True,
    )
    cor_primaria: Mapped[str | None] = mapped_column(
        String(30),
        nullable = True,
    )
    cor_secundaria: Mapped[str | None] = mapped_column(
        String(30),
        nullable = True,
    )
    cor_terciaria: Mapped[str | None] = mapped_column(
        String(30),
        nullable = True,
    )
    website: Mapped[str | None] = mapped_column(
        String(2048),
        nullable = True,
    )
    escudo: Mapped[str | None] = mapped_column(
        String(2048),
        nullable = True,
    )
    descricao: Mapped[str | None] = mapped_column(
        Text,
        nullable = True,
    )
    ativo: Mapped[bool] = mapped_column(
        Boolean,
        nullable = False,
        default = True,
        server_default = true(),
    )
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        nullable = False,
        server_default = func.now(),
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        nullable = False,
        server_default = func.now(),
        onupdate = func.now(),
    )


