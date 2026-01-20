import os 

import logging

log_level =  os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(
	level=log_level,
	format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING messsage")
logging.error("This is an ERROR message")

