from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.db.database import Base

class Spending(Base):
    __tablename__ = 'spendings'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)  # e.g., Food, Transport, etc.
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)

    # Foreign key to link spending to a user
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    owner = relationship("User", back_populates="spendings")
