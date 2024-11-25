# database.py

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
import configparser
from logger import logger  # Import the logger

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

try:
    db_config = config['database']
    # Use PyMySQL driver and specify charset
    DB_URL = (
        f"mysql+pymysql://{db_config['username']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database_name']}?charset=utf8mb4"
    )

    # Set pool_recycle and pool_timeout to handle dropped connections and timeouts
    engine = create_engine(
        DB_URL,
        pool_pre_ping=True,
        pool_recycle=3600,  # Recycle connections after 1 hour
        pool_timeout=30,    # Wait max 30 seconds for a connection
        echo=False          # Set to True to enable SQL echoing
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Database connection established")
except exc.SQLAlchemyError as e:
    logger.exception(f"SQLAlchemy error during engine creation: {e}")
    raise
except Exception as e:
    logger.exception(f"Unexpected error during database setup: {e}")
    raise
