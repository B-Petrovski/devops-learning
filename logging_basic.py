import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="app.log",
    filemode="w"
)

logging.debug("This is a debug message")
logging.info("Script started successfully")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("Critical failure")

