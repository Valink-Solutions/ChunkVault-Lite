import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

DETA_PROJECT_KEY = os.getenv("DETA_PROJECT_KEY", "")
