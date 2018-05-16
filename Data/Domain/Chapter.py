from sqlalchemy.orm import relationship, backref

from Data.Domain.ChapterLesson import ChapterLesson
from Data.Domain.ChapterExercise import ChapterExercise
from Data.Persistance.database import Base
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey

from sqlalchemy.dialects.mysql import MEDIUMTEXT




class Chapter(Base):
    __tablename__ = 'chapter'
    id = Column(Integer(), primary_key=True)
    title = Column(String(50))

    lessons = relationship(ChapterLesson, uselist=False)
    exercises = relationship(ChapterExercise, uselist=False)