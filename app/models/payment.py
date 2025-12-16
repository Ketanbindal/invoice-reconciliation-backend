from sqlalchemy import Column, Integer, String, Numeric, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    transaction_date = Column(Date, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    narration = Column(String, nullable=True)

    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=True)

    is_reconciled = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
