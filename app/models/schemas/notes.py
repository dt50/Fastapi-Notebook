from typing import List, Optional
from pydantic import BaseModel


class NoteIn(BaseModel):
    title: str
    description: str


class NoteOut(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]


class NotesList(BaseModel):
    notes: List[NoteOut]


class NoteUpdate(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]


class NoteDelete(BaseModel):
    id: int
