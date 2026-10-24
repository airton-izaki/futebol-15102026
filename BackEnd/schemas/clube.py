from datetime   import date, datetime
from enum       import Enum
from pydantic   import BaseModel, ConfigDict, Field, field_validator, HttpUrl

class GestaoClube(str, Enum):
    ASSOCIATIVO = "Associativo"
    HIBRIDO = "Híbrido"
    PRIVADO = "Privado"
    SAF = "SAF"     
    
class ClubeCreate(BaseModel):

    """Dados necessários para cadastrar um clube."""
    model_config = ConfigDict(extra = "forbid")

    nome_oficial: str = Field(min_length = 1, max_length = 100)
    nome: str = Field(min_length = 1, max_length = 100)
    sigla: str = Field(min_length = 1, max_length = 5)
    gestao: GestaoClube = GestaoClube.ASSOCIATIVO
    fundacao: date
    codigo_ibge_municipio: int = Field(gt = 0)
    estadio: str | None = Field(default = None, max_length = 100)
    cor_principal: str | None = Field(default = None, max_length = 30)
    cor_secundaria: str | None = Field(default = None, max_length = 30)
    cor_terciaria: str | None = Field(default = None, max_length = 30)
    website: HttpUrl | None = None
    escudo: HttpUrl | None = None
    descricao: str | None = None
    ativo: bool = True

    @field_validator("nome_oficial", "nome", "sigla")
    @classmethod
    def remover_espacos_extremos(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("Este campo não pode ficar vazio")

        return valor

"""Dados devolvidos pela API após consultar um clube."""
class ClubeResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id: int
    nome_oficial: str
    nome: str
    sigla: str
    gestao: GestaoClube
    fundacao: date
    codigo_ibge_municipio: int
    cidade: str
    estado_nome: str
    estado_sigla: str
    estadio: str | None
    cor_principal: str | None = Field(validation_alias = "cor_primaria")
    cor_secundaria: str | None
    cor_terciaria: str | None
    website: str | None
    escudo: str | None
    descricao: str | None
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime

    @field_validator("gestao", mode = "before")
    @classmethod
    def converter_gestao_do_banco(cls, valor):
        if isinstance(valor, str) and valor in GestaoClube.__members__:
            return GestaoClube[valor]
        return valor
