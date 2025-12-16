from fastapi import FastAPI
from app.api.v1.routes.invoices import router as invoice_router
from app.api.v1.routes.payments import router as payment_router
from app.api.v1.routes.reconcile import router as reconcile_router

app = FastAPI(title="Invoice Reconciliation Backend")

app.include_router(invoice_router, prefix="/api/v1/invoices")
app.include_router(payment_router, prefix="/api/v1/payments")
app.include_router(reconcile_router, prefix="/api/v1/reconcile")
