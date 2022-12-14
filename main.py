from database import engine, Base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth


app = FastAPI()

app.add_middleware(CORSMiddleware, 
allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
