from sqlalchemy import Column, Integer, String, Time
from src.models.base import Base

class LembreteTable(Base):
    __tablename__ = "lembretes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    quantidade = Column(Integer, nullable=False)
    horario = Column(Time, nullable=False)
