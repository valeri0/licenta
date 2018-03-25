from Data.Persistance.database import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(512))
    active = Column(Boolean())
    role_id = Column(Integer(),ForeignKey('role.id'))
    role = relationship('Role')
