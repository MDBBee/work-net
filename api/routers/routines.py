from pydantic import BaseModel
from typing import List, Optional
from fastapi import APIRouter
from sqlalchemy.orm import joinedload
from api.models import Workout, Routine
from api.deps import user_dependency, db_dependency


router = APIRouter(
    prefix="/routines",
    tags=["routines"]
)


class RoutineBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoutineCreate(RoutineBase):
    pass