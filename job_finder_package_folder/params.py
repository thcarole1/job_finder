import os

##################  VARIABLES  ##################
# France Travail
FT_CLIENT_ID = os.environ.get("FT_CLIENT_ID")
FT_CLIENT_SECRET = os.environ.get("FT_CLIENT_SECRET")
FT_SCOPE = os.environ.get("FT_SCOPE")

# Adzuna
ADZUNA_CLIENT_ID = os.environ.get("ADZUNA_CLIENT_ID")
ADZUNA_CLIENT_SECRET = os.environ.get("ADZUNA_CLIENT_SECRET")


# Param Database PostgreSQL
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
