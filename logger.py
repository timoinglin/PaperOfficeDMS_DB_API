# logger.py

import logging
from logging.handlers import RotatingFileHandler

# Create a logger object
logger = logging.getLogger('paperoffice_api')
logger.setLevel(logging.INFO)

# Create a rotating file handler
log_file = 'paperoffice_api.log'
max_file_size = 5 * 1024 * 1024  # 5 MB
backup_count = 2  # Keep 2 backup log files

rotating_handler = RotatingFileHandler(
    log_file, maxBytes=max_file_size, backupCount=backup_count
)
rotating_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
rotating_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(rotating_handler)
