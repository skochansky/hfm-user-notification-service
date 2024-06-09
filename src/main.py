from fastapi import FastAPI
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with PostgreSQL"}

