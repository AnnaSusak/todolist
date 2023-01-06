import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from config import config as c

engine = create_async_engine(c.db_url)
Base = declarative_base()
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# модели
class Note(Base):
    __tablename__ = 'notes'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    checked = sa.Column(sa.Boolean, nullable=False)


__all__ = ['engine', 'Base', 'async_session', 'Note']
