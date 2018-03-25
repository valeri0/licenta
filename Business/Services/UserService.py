from Business.Repositories.UserRepository import UserRepository
from Data.Domain.User import User


class UserService:
    __user_repository = UserRepository()

    def create_user(self, email, password, role):
        user = User()
        user.email = email
        user.password = password
        user.roles_users.append(role)

        self.__user_repository.create_user(user)
