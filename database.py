from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()



class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String,index=True)
    email=Column(String,unique=True,index=True)
Base.metadata.create_all(bind=engine)