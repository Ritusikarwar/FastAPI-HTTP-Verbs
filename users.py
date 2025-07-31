from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from routes.database import SessionLocal,User 
from routes.schemas import Users,StudentOut
from pydantic import BaseModel
from typing import List


router = APIRouter()

class Users(BaseModel):
    id: int
    username: str
    email: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/users/")
async def create_user(input_request: Users,db:Session=Depends(get_db)):
    new_user = User(
        id=input_request.id,
        username=input_request.username,
        email=input_request.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }


@router.patch("/users/{user_id}")
async def update_user(user_id: int, input_request: Users, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == user_id).first()
    if user_data:
        user_data.username = input_request.username
        user_data.email = input_request.email
        db.commit()
        return {"message": "User updated"}
    else:
        return {"message": "User not found"}



@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == user_id).first()
    if user_data:
        db.delete(user_data)
        db.commit()
        return {"message": "User deleted"}
    else:
        return {"message": "User not found"}




@router.get("/users/", response_model=List[StudentOut])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
