from fastapi import FastAPI

from app.database import Base, engine
from app.routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth API")

app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Auth API is running"}