import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CLIENT_ID = os.getenv("CLIENT_ID")
