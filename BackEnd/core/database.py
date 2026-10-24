import os
from sqlalchemy             import create_engine
from sqlalchemy.orm         import DeclarativeBase, sessionmaker

# 1. Definindo o caminho do arquivo do SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./banco.db"

# 2. Criando a Engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# 3. Configurando a fábrica de sessões (SessionLocal)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine,
)

# 4. Sua classe Base para os modelos
class Base(DeclarativeBase):
    pass

# 5. Função de dependência para injetar a sessão nas rotas do FastAPI
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
