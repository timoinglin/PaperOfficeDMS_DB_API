# routers/contacts.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Contact
from auth import AuthBearer
from logger import logger

router = APIRouter(
    prefix="/contacts",
    tags=["Contacts"],
    dependencies=[Depends(AuthBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", summary="Retrieve a list of contacts")
def read_contacts(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0), db: Session = Depends(get_db)):
    """
    Retrieve a list of contacts with pagination.

    - **limit**: The number of contacts to return (default is 10).
    - **offset**: The number of contacts to skip (default is 0).
    """
    try:
        contacts = db.query(Contact).limit(limit).offset(offset).all()
        logger.info(f"Retrieved {len(contacts)} contacts")
        return contacts
    except Exception as e:
        logger.exception(f"Error retrieving contacts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{contact_id}", summary="Retrieve a contact by ID")
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single contact by its ID.

    - **contact_id**: The ID of the contact to retrieve.
    """
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        logger.warning(f"Contact with ID {contact_id} not found")
        raise HTTPException(status_code=404, detail="Contact not found")
    logger.info(f"Retrieved contact with ID {contact_id}")
    return contact

