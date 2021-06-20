from sqlalchemy import Column, BIGINT, TEXT, DECIMAL, BOOLEAN, false
from .base import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(BIGINT, primary_key=True)
    
    tg_id = Column(BIGINT, nullable=False, unique=True)
    username = Column(TEXT, nullable=True, unique=True)
    
    banned = Column(BOOLEAN, nullable=False, default=false())
    
    def __repr__(self):
        return f"User({self.tg_id}, {self.username}, {self.banned})"
