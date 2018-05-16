from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean
from Data.Persistance.database import Base


class ChapterExercise(Base):
    __tablename__ = 'chapter_exercise'
    exercise_id = Column(Integer, ForeignKey("exercise.id"), primary_key=True)
    chapter_id = Column(Integer, ForeignKey("chapter.id"), primary_key=True)
