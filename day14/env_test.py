import os

env = os.getenv("APP_ENV")

if env is None:
	print("APP_ENV is not set")
else:
	print(f"Application running in {env} mode")

