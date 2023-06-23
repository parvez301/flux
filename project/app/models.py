from sqlmodel import SQLModel, Field
from typing import Optional


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None
    created_on: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(default=None, primary_key=True)


class SongCreate(SongBase):
    pass