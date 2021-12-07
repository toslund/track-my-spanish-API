# from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401

class Lemma(Base):
    __tablename__ = 'lemma'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ## TODO change to uuid type in production
    uuid = Column(String(36), nullable=False, unique=True)
    lemma = Column(String(50), nullable=False)
    pos = Column(String(10), nullable=True)
    rank = Column(Integer, nullable=True)

    total_count = Column(Integer, nullable=True)
    academic_count = Column(Integer, nullable=True)
    news_count = Column(Integer, nullable=True)
    fiction_count = Column(Integer, nullable=True)
    spoken_count = Column(Integer, nullable=True)

    note_data = Column(String(), nullable=True)
    note_qaqc = Column(String(), nullable=True)
    note_grammar = Column(String(), nullable=True)
    note = Column(String(), nullable=True)
    
    date_added = Column(DateTime, nullable=True)
    date_deprecated = Column(DateTime, nullable=True)
    ## relationship
    ## one lemma -> many vocabs
    vocabs = relationship("Vocab", back_populates="lemma")

