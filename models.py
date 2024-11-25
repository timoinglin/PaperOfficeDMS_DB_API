# models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    Text,
    DateTime,
    Float,
    DECIMAL,
    LargeBinary,
    Boolean,
)
# No need to import logger here unless you plan to log from models

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer)
    name = Column(String(200))
    description = Column(String(5000))
    # Add other fields as necessary

class Document(Base):
    __tablename__ = 'documents'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(250))
    category = Column(String(250))
    added_datetime = Column(DateTime)
    file_extension = Column(String(250))
    # Add other fields as necessary

class DocumentOCR(Base):
    __tablename__ = 'documents_ocr'

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(BigInteger, index=True)
    version = Column(Float)  # Ensure this is correctly declared
    language = Column(String(5))
    baselanguage = Column(String(5))
    ocr_text = Column(Text)
    added_datetime = Column(DateTime)
    # Add other fields as necessary

class PaperOfficeAccount(Base):
    __tablename__ = 'paperoffice_account'

    id = Column(Integer, primary_key=True, index=True)
    paperoffice_account_id = Column(BigInteger)
    email = Column(String(250))
    name = Column(String(250))
    # Add other fields as necessary

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    section = Column(String(50))
    name = Column(String(100))
    firstname = Column(String(100))
    lastname = Column(String(100))
    company = Column(String(100))
    personal_email = Column(String(100))
    company_email = Column(String(100))
    # Add other fields as necessary
