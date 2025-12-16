from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_payments():
    return {"message": "Payments upload endpoint placeholder"}
