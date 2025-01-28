from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database_session import Base
from core.env_settings import EnvironmentSettings

DB_URL = f"postgresql://{EnvironmentSettings.SQL_DB_USERNAME}:{EnvironmentSettings.SQL_DB_PASSWORD}@{EnvironmentSettings.SQL_DB_HOST}:{EnvironmentSettings.SQL_DB_PORT}/{EnvironmentSettings.SQL_DB_NAME}"
print(DB_URL)
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)
Session = SessionLocal()
SqlBase = Base
