import logging 
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
	"rotating.log",
	maxBytes=100,
	backupCount=5
)

formatter = logging.Formatter(
	"%(asctime)s  [%(levelname)s] %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(20):
	logger.info(f"Log message number {i}")
