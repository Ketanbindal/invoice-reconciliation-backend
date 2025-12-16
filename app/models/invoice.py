from sqlalchemy import Column, Integer, String, Numeric, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base
import enum


class InvoiceStatus(str, enum.Enum):
    PAID = "PAID"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    PENDING = "PENDING"
    OVERPAID = "OVERPAID"


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    invoice_number = Column(String, nullable=False, unique=True, index=True)
    customer_name = Column(String, nullable=False)

    total_amount = Column(Numeric(12, 2), nullable=False)
    cash_received = Column(Numeric(12, 2), default=0)

    pending_amount = Column(Numeric(12, 2), nullable=False)

    status = Column(
        Enum(InvoiceStatus),
        default=InvoiceStatus.PENDING,
        nullable=False
    )

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
