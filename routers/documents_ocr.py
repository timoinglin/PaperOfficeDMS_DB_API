# routers/documents_ocr.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import DocumentOCR
from auth import AuthBearer
from logger import logger

router = APIRouter(
    prefix="/documents_ocr",
    tags=["Documents OCR"],
    dependencies=[Depends(AuthBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{document_id}", summary="Retrieve OCR data for a document")
def read_document_ocr(document_id: int, db: Session = Depends(get_db)):
    """
    Retrieve OCR data for a document by its ID.

    - **document_id**: The ID of the document.
    """
    ocr_entries = db.query(DocumentOCR).filter(DocumentOCR.document_id == document_id).all()
    if not ocr_entries:
        logger.warning(f"OCR data for document ID {document_id} not found")
        raise HTTPException(status_code=404, detail="OCR data not found for the specified document ID")
    logger.info(f"Retrieved OCR data for document ID {document_id}")
    return ocr_entries