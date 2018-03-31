from Business.Repositories.UserRepository import UserRepository
from Data.Domain.User import User
from Data.Domain.Role import Role


class UserService:
    __user_repository = UserRepository()

    def create_user(self, email, password, _role):
        user = User()
        user.email = email
        user.password = password

        role = Role()
        role.name = _role
        user.role = role

        self.__user_repository.create_user(user)
