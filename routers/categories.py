# routers/categories.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Category
from auth import AuthBearer
from logger import logger

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    dependencies=[Depends(AuthBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", summary="Retrieve a list of categories")
def read_categories(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0), db: Session = Depends(get_db)):
    """
    Retrieve a list of categories with pagination. (Directories)

    - **limit**: The number of categories to return (default is 10).
    - **offset**: The number of categories to skip (default is 0).
    """
    try:
        categories = db.query(Category).limit(limit).offset(offset).all()
        logger.info(f"Retrieved {len(categories)} categories")
        return categories
    except Exception as e:
        logger.exception(f"Error retrieving categories: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
