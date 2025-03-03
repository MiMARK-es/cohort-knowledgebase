import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://cohorts_db_user:LNdjcSkFYnBPqeNAifTfUlihgtQY81FU@dpg-cv2nq2dsvqrc7395t2n0-a/cohorts_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()