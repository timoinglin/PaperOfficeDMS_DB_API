# app.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import test, categories, documents, documents_ocr, paperoffice_account, contacts
from logger import logger

app = FastAPI(
    title="PaperOfficeDMS API",
    description="API for retrieving information from PaperOffice DB",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to be more restrictive in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(test.router)
app.include_router(documents.router)
app.include_router(documents_ocr.router)
app.include_router(categories.router)
app.include_router(contacts.router)
app.include_router(paperoffice_account.router)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )