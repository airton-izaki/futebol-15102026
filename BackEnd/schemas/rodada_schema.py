from datetime       import datetime
from typing         import Optional
from pydantic       import BaseModel, ConfigDict, Field


class RodadaBase(BaseModel):
    model_config = ConfigDict(extra = "forbid")

    campeonato_id: int = Field(
        ..., gt = 0, 
        description = "ID do campeonato ao qual a rodada pertence"
    )

    numero: int = Field(
        ..., 
        gt = 0, 
        description = "Número da rodada (Ex: 1 para 1ª Rodada)"
    )

    ativa: bool = Field(
        default = False, 
        description = "Indica se a rodada está ativa no momento"
    )

# 1. Schema para a ENTRADA de dados (POST do Angular)
class RodadaCreate(RodadaBase):
    pass

# 2. Schema para Atualização (PUT/PATCH)
class RodadaUpdate(BaseModel):
    model_config = ConfigDict(extra = "forbid")

    campeonato_id: Optional[int] = Field(default = None, gt = 0)
    numero: Optional[int] = Field(default = None, gt = 0)
    ativa: Optional[bool] = None


# 3. Schema para a SAÍDA de dados (Response básico)
class RodadaResponse(RodadaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int






