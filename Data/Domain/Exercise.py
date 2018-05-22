from sqlalchemy.orm import relationship, backref
from Data.Domain.UserExerciseDifficulty import UserExerciseDifficulty
import Data.Persistance.database as db
from Data.Domain.Chapter import Chapter

from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey, Float

from sqlalchemy.dialects.mysql import MEDIUMTEXT


class Exercise(db.Base):
    __tablename__ = 'exercise'
    id = Column(Integer(),primary_key=True)
    title = Column(String(50))
    content = Column(MEDIUMTEXT())
    source_code = Column(MEDIUMTEXT())
    default_elo_rating = Column(Float())

    user_exercise_difficulty = relationship(UserExerciseDifficulty,uselist=False)

