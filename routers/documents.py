# routers/documents.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal
from models import Document
from auth import AuthBearer
from logger import logger

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
    dependencies=[Depends(AuthBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", summary="Retrieve a list of documents")
def read_documents(
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    name: Optional[str] = Query(None, description="Search for documents by name"),
    db: Session = Depends(get_db)
):
    """
    Retrieve a list of documents with pagination. Optionally search by document name.

    - **limit**: The number of documents to return (default is 10).
    - **offset**: The number of documents to skip (default is 0).
    - **name**: A string to search for in document names.
    """
    try:
        query = db.query(Document)
        if name:
            query = query.filter(Document.name.ilike(f"%{name}%"))
        documents = query.limit(limit).offset(offset).all()
        logger.info(f"Retrieved {len(documents)} documents")
        return documents
    except Exception as e:
        logger.exception(f"Error retrieving documents: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{document_id}", summary="Retrieve a document by ID")
def read_document(document_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single document by its ID.

    - **document_id**: The ID of the document to retrieve.
    """
    document = db.query(Document).filter(Document.id == document_id).first()
    if document is None:
        logger.warning(f"Document with ID {document_id} not found")
        raise HTTPException(status_code=404, detail="Document not found")
    logger.info(f"Retrieved document with ID {document_id}")
    return document

