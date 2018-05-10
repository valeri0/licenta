from sqlalchemy import Column, Integer, ForeignKey

from Data.Persistance.database import Base


class UserLessonDifficulty(Base):
    """
    Class used to link a :class:`User` to a :class:`Lesson`
    and have a custom difficulty (Elo rating) between them

    Example: We want that each user to have the same lessons,
    but with different difficulty, customized by the user's progress so far.
    """

    __tablename__ = 'user_lesson_difficulty'
    user_id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"),primary_key=True)
    elo_rating = Column(Integer(),nullable=False)
