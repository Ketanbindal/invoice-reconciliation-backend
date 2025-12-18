from fastapi import APIRouter
from app.api.deps import get_current_user
from app.models.user import User
from fastapi import Depends


router = APIRouter()


@router.get("/health")
def invoice_health(current_user: User = Depends(get_current_user)):
    return {"status": "secured", "user_id": current_user.id}

@router.post("/upload")
def upload_invoices(current_user: User = Depends(get_current_user)):
    return {"message": "Invoices upload endpoint placeholder"}
