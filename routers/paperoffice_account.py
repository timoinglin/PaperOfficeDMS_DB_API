# routers/paperoffice_account.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from models import PaperOfficeAccount
from auth import AuthBearer
from logger import logger

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
    dependencies=[Depends(AuthBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", summary="Retrieve a list of accounts")
def read_accounts(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0), db: Session = Depends(get_db)):
    """
    Retrieve a list of PaperOffice accounts with pagination.

    - **limit**: The number of accounts to return (default is 10).
    - **offset**: The number of accounts to skip (default is 0).
    """
    try:
        accounts = db.query(PaperOfficeAccount).limit(limit).offset(offset).all()
        logger.info(f"Retrieved {len(accounts)} accounts")
        return accounts
    except Exception as e:
        logger.exception(f"Error retrieving accounts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{account_id}", summary="Retrieve an account by ID")
def read_account(account_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single account by its ID.

    - **account_id**: The ID of the account to retrieve.
    """
    account = db.query(PaperOfficeAccount).filter(PaperOfficeAccount.id == account_id).first()
    if account is None:
        logger.warning(f"Account with ID {account_id} not found")
        raise HTTPException(status_code=404, detail="Account not found")
    logger.info(f"Retrieved account with ID {account_id}")
    return account