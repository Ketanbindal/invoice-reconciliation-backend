import os

class Settings:
    PROJECT_NAME = "Invoice Reconciliation Backend"
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/recon_db")

settings = Settings()
