from datetime           import datetime
from sqlalchemy         import Boolean , DateTime, func, String, true
from sqlalchemy.orm     import Mapped, mapped_column
from core.database      import Base



class Campeonato(Base):
    __tablename__ = "campeonato"    # Define o nome da tabela no banco


    id: Mapped[int] = mapped_column(
        primary_key = True,
        index = True,    
    )

    nome_campeonato: Mapped[str] = mapped_column(
        String(100),
        nullable = False,
        comment = "Ex: Campeonato Brasileiro - Série A", 
    )

    temporada: Mapped[str] = mapped_column(
        String(10),
        nullable = False,
        comment = "Ex: 2026 ou 2025/2026",
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