from database import engine, Base
from fastapi import FastAPI
from routers import auth


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
