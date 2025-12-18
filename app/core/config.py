import os

class Settings:
    PROJECT_NAME = "Invoice Reconciliation Backend"
    API_V1_STR = "/api/v1"
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@db:5432/recon_db"
    )

settings = Settings()
