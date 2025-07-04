from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


workout_db_url = "sqlite:///workout.db"
engine= create_engine(workout_db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()