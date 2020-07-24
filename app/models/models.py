from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    usr_login: str = Field(..., min_length=0, max_length=50)
    usr_password1: str = Field(..., min_length=0, max_length=50)
    usr_password2: str = Field(..., min_length=0, max_length=50)


class UserLog(BaseModel):
    usr_login: str = Field(..., min_length=0, max_length=50)
    usr_password: str = Field(..., min_length=0, max_length=50)


class NoteSchema(BaseModel):
    usr_login: str = Field(..., min_length=0, max_length=50)
    usr_password: str = Field(..., min_length=0, max_length=50)

    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)


class ChangeNoteSchema(BaseModel):
    id: int = Field(...,)
    usr_login: str = Field(..., min_length=0, max_length=50)
    usr_password: str = Field(..., min_length=0, max_length=50)

    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
