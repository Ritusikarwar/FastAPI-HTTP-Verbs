from pydantic import BaseModel

class Users(BaseModel):
    id: int
    username: str
    email: str

class StudentCreate(Users):
    pass

class StudentOut(Users):
    id: int
    class Config:
        orm_mode = True
