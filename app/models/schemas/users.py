from pydantic import BaseModel, Field


class UserIn(BaseModel):
    login: str = Field(..., min_length=0, max_length=50)
    password: str = Field(..., min_length=0, max_length=50)


class UserOut(BaseModel):
    login: str = None
    id: int = None
