# routers/test.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from logger import logger
import datetime

# Define the APIRouter
router = APIRouter(
    prefix="/ping",
    tags=["Test"],
    responses={404: {"description": "Not found"}},
)

# Define the response model
class PingResponse(BaseModel):
    message: str
    status: str
    server_time: str

@router.get("/", summary="Test endpoint to check server responsiveness", response_model=PingResponse)
def ping():
    """
    A simple test endpoint that returns "pong" along with the server time.

    - **message**: Response message (e.g., "pong").
    - **status**: Indicates success or failure.
    - **server_time**: Current server time in ISO 8601 format (UTC).
    """
    try:
        message = "pong"
        status = "success"
        server_time = datetime.datetime.now(datetime.timezone.utc).isoformat() + 'Z'  # UTC time in ISO 8601 format
        logger.info(f"Ping successful at {server_time}")
        return {"message": message, "status": status, "server_time": server_time}
    except Exception as e:
        logger.exception(f"Error in ping endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
