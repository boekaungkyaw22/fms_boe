from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.db.database import Base

class BalanceHistory(Base):
    __tablename__ = 'balance_history'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    remaining_balance = Column(Float, nullable=False)

    # Foreign key to link balance history to a user
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    owner = relationship("User", back_populates="balance_history")
