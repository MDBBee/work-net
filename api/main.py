from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .routers import auth, workouts

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)


@app.get("/")
def health_check():
    return "Health check complete"

app.include_router(auth.router)
app.include_router(workouts.router)