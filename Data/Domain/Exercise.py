from sqlalchemy.orm import relationship, backref

import Data.Persistance.database as db
from Data.Domain.Chapter import Chapter

from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey

from sqlalchemy.dialects.mysql import MEDIUMTEXT


class Exercise(db.Base):
    __tablename__ = 'exercise'
    id = Column(Integer(),primary_key=True)
    title = Column(String(50))
    content = Column(MEDIUMTEXT())
    source_code = Column(MEDIUMTEXT())

