# main.py

import uvicorn
import configparser
from logger import logger

config = configparser.ConfigParser()
config.read('config.ini')
server_config = config['server']

if __name__ == "__main__":
    logger.info("Starting PaperOfficeDMS API server")
    uvicorn.run(
        "app:app",
        host=server_config.get('host', '0.0.0.0'),
        port=int(server_config.get('port', 8000)),
        reload=server_config.getboolean('development', True)
    )
