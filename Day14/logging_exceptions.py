import logging

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s [%(levelname)s] %(message)s",
	filename="app.log",
	filemode="a"
)
def divide (a, b):
	return a / b

logging.info("starting division test")

try:
	result = divide(10, 0)
	logging.info(f"Result is {result}")
except Exception:
	logging.exception("An error occurred during division")

logging.info("Script finished")


