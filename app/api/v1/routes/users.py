from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/account")
def invoice_health(current_user: User = Depends(get_current_user)):
    return {"status": "secured", "user_id": current_user.id}

@router.post(
    "/create_user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
):
    user = User(
        email=user_in.email,
        password_hash=hash_password(user_in.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user