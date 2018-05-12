from Business.Repositories.UserRepository import UserRepository
from Data.Domain.User import User
from Data.Domain.Role import Role
from flask.ext import bcrypt


class UserService:
    __user_repository = UserRepository()

    def create_user(self, email, password, _role):
        user = User()
        user.email = email
        user.password = bcrypt.generate_password_hash(password)

        role = Role()
        role.name = _role
        user.role = role

        self.__user_repository.create_user(user)

    def logout_user(self,user):
        self.__user_repository.create_user(user)

    def get_user_by_id(self,user_id):
        return self.__user_repository.get_user_by_id(user_id)

    def get_current_user_id(self):
        return self.get_current_user_id()