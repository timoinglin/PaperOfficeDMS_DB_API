# auth.py

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import configparser
from logger import logger

config = configparser.ConfigParser()
config.read('config.ini')
AUTH_TOKEN = config['auth']['token']

class AuthBearer(HTTPBearer):
    async def __call__(self, request: Request):
        try:
            credentials: HTTPAuthorizationCredentials = await super(AuthBearer, self).__call__(request)
            if credentials:
                if credentials.scheme != "Bearer":
                    logger.warning("Invalid authentication scheme")
                    raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
                if credentials.credentials != AUTH_TOKEN:
                    logger.warning("Invalid token or expired token")
                    raise HTTPException(status_code=403, detail="Invalid token or expired token.")
                return credentials.credentials
            else:
                logger.warning("No credentials provided")
                raise HTTPException(status_code=403, detail="Invalid authorization code.")
        except HTTPException as e:
            logger.error(f"Authentication error: {e.detail}")
            raise
        except Exception as e:
            logger.exception(f"Unexpected error during authentication: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
