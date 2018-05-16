from sqlalchemy import Column, Integer, ForeignKey
from Data.Persistance.database import Base


class ChapterLesson(Base):
    __tablename__ = 'chapter_lesson'
    chapter_id = Column(Integer, ForeignKey("chapter.id"), primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"), primary_key=True)
