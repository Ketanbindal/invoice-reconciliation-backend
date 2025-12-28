from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import auth, invoices, payments, reconcile, users
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(invoices.router, prefix=settings.API_V1_STR)
app.include_router(payments.router, prefix=settings.API_V1_STR)
app.include_router(reconcile.router, prefix=settings.API_V1_STR)
app.include_router(users.router, prefix=settings.API_V1_STR)
