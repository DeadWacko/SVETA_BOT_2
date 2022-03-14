from sqlalchemy import Column, String, ForeignKey, Table, BIGINT
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    __tablename__ = 'users'
    telegram_id = Column(BIGINT, primary_key=True)
    teacher_id = Column(String)
    time = Column(String)
    team = Column(String)
    fullname = Column(String)



    # teacher = relationship("Teacher", back_populates="tg_user")
    # student = relationship("Student", back_populates="tg_user")


