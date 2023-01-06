from pydantic import BaseSettings


class Config(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///todolistdb.db'
    host: str = '127.0.0.1'
    port: int = 1874


config = Config(_env_file='.env')

__all__ = ['config']
