from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_invoices():
    return {"message": "Invoices upload endpoint placeholder"}
