from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Cohort(Base):
    __tablename__ = "cohorts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Sample(Base):
    __tablename__ = "samples"
    id = Column(Integer, primary_key=True, index=True)
    cohort_id = Column(Integer, ForeignKey("cohorts.id"))
    value = Column(String)
    cohort = relationship("Cohort")
