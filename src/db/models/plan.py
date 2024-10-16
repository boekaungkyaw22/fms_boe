from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.db.database import Base

class Plan(Base):
    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True, index=True)
    goal_name = Column(String, nullable=False)  # e.g., Vacation, New Phone
    target_amount = Column(Float, nullable=False)
    current_savings = Column(Float, default=0.0)
    deadline = Column(Date, nullable=True)

    # Foreign key to link plan to a user
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    owner = relationship("User", back_populates="plans")
