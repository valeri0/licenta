from flask_login import current_user
from Business.Repositories.HomeworkRepository import HomeworkRepository

class HomeworkService:
    _homework_repository = HomeworkRepository()

    def get_homework_by_id(self,homework_id):
        return self._homework_repository.get_homework_by_id(homework_id)

    def get_incomplete_homeworks_for_user(self):
        '''

        :return: (user_homework_difficulty,homework)
        '''

        result = []

        incomplete_homweorks =  self._homework_repository.get_incomplete_homeworks_for_user(current_user.id)

        for x in incomplete_homweorks:
            result.append((x,self._homework_repository.get_homework_by_id(x.homework_id)))

        return result

    def get_temporary_code_for_homework(self,homework_id):
        user_id = current_user.id
        return self._homework_repository.get_temporary_code_for_homework(user_id,homework_id)