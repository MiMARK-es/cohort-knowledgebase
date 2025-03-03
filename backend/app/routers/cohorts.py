from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Cohort

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/cohorts")
def read_cohorts(db: Session = Depends(get_db)):
    return db.query(Cohort).all()
