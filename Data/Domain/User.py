from Data.Persistance.database import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey

from flask.ext import bcrypt


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(512))
    elo_rating = Column(Integer())
    active = Column(Boolean())
    role_id = Column(Integer(), ForeignKey('role.id'))
    role = relationship('Role')
    is_authenticated = True

    def is_authenticated(self):
        return self.is_authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.password, input_password)

    def get_display_name(self):
        return self.email[:self.email.index('@')]
