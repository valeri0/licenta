from Data.Persistance.database import *
from Data.Domain import User, Role
from flask_security import SQLAlchemySessionUserDatastore


class UserRepository:
    __user_datastore = SQLAlchemySessionUserDatastore(db_session, User.User, Role.Role)
    db_context = db_session

    def get_user_datastore(self):
        return self.__user_datastore

    def create_user(self,user):
        self.db_context.add(user)


