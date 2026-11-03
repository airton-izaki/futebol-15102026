from datetime                   import date, time
from typing                     import Optional
from pydantic                   import BaseModel, ConfigDict, Field
from schemas.rodada_schema      import RodadaResponse
from schemas.campeonato_shcema  import CampeonatoResponse
from schemas.clube              import ClubeResponse




# Schema Base: atributos compartilhados
class JogoBase(BaseModel):
    campeonato_id: int
    rodada_id: int
    time_mandante_id: str
    time_visitante_id: str
    local: Optional[str] = None
    data_jogo: date
    hora_jogo: time
    observacao: Optional[str] = None

# Schema para Criação (POST)
class JogoCreate(JogoBase):
    pass


# Schema para Atualização (PUT/PATCH)
class JogoUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campeonato_id: Optional[int] = Field(..., gt = 0)
    rodada_id: Optional[int] = Field(default = None, gt = 0)
    time_mandante_id: Optional[str] = Field(..., min_length = 1)
    time_visitante_id: Optional[str] = Field(..., min_length = 1)
    local: Optional[str] = Field(default = None, max_length = 150)
    data_jogo: date
    hora_jogo: time
    observacao: Optional[str] = Field(default = None, max_length = 500)


# 2. Schema para Criação (POST)
class JogoCreate(JogoBase):
    pass


# 3. Schema para Atualização (PUT/PATCH)
class JogoUpdate(BaseModel):
    model_config = ConfigDict(extra = "forbid")

    campeonato_id: Optional[int] = Field(default = None, gt = 0)
    rodada_id: Optional[int] = Field(default = None, gt = 0)
    time_mandante_id: Optional[str] = Field(default = None, min_length = 1)
    time_visitante_id: Optional[str] = Field(default = None, min_length = 1)
    local: Optional[str] = Field(default = None, max_length = 150)
    data_jogo: Optional[date] = None
    hora_jogo: Optional[time] = None
    observacao: Optional[str] = Field(default = None, max_length = 500)


# 4. Schema de Resposta 
class JogoResponse(JogoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


# 5. Schema de Resposta Detalhada (Com os objetos completos para o Angular)
class JogoDetailResponse(JogoResponse):
    campeonato: Optional[CampeonatoResponse] = None
    rodada: Optional[RodadaResponse] = None
    time_mandante: Optional[ClubeResponse] = None
    time_visitante: Optional[ClubeResponse] = None
    
    # Flag para o front saber se exibe "Cadastrar Súmula" ou "Ver Súmula"
    tem_sumula: bool = False

