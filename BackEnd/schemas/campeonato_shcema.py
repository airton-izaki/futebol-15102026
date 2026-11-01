from datetime           import date, datetime
from pydantic           import BaseModel, Field

# 1. Schema para a ENTRADA de dados (O que o Angular envia no POST)
class CampeonatoCreate(BaseModel):
    nome_campeonato: str = Field(
        ...,
        min_length = 1,
        max_length = 100,
        example="Campeonato Brasileiro - Série A",
    )

    temporada: str = Field(
        ...,
        min_length = 1,
        max_length = 10
        example="2026 ou 2025/2026",
    )

    ativo: bool = True

# 2. Schema para a SAÍDA de dados (O que o FastAPI devolve para o Angular)
class CampeonatoResponse(BaseModel):
    id: int
    nome_campeonato: str
    temporada: str
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime

class Config:
    from_attributes = True
    