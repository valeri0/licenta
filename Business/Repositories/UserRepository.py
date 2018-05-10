from Data.Persistance.database import *
from Data.Domain.User import User
from Data.Domain.Role import Role
from flask_security import SQLAlchemySessionUserDatastore


class UserRepository:
    __user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
    db_context = db_session

    def get_user_datastore(self):
        return self.__user_datastore

    def create_user(self, user):
        self.db_context.add(user)
        self.db_context.commit()

    def get_user_by_id(self, user_id):
        return User.query.filter(User.id == user_id).first()
