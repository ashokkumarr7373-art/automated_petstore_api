import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://petstore.swagger.io/v2")
