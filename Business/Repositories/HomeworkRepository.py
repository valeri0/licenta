from Data.Persistance.database import *
from Data.Domain.Homework import Homework
from Data.Domain.UserHomeworkDifficulty import UserHomeworkDifficulty

class HomeworkRepository:
    _db_context = db_session

    def get_homework_by_id(self,homework_id):
        return Homework.query.filter_by(id=homework_id).first()

    def get_homework_for_user(self,user_id,homework_id):
        return UserHomeworkDifficulty.query.filter_by(user_id=user_id,homework_id=homework_id).first()

    def get_incomplete_homeworks_for_user(self,user_id):
        return UserHomeworkDifficulty.query.filter(UserHomeworkDifficulty.user_id == user_id,UserHomeworkDifficulty.completed == 0).order_by(UserHomeworkDifficulty.days_remaining.asc()).all()

    def update_temporary_code(self,user_id,homework_id,source_code):
        user_homework_difficulty = self.get_homework_for_user(user_id,homework_id)
        user_homework_difficulty.temporary_code = source_code
        self._db_context.commit()

    def get_temporary_code_for_homework(self,user_id,homework_id):
        return UserHomeworkDifficulty.query.filter_by(user_id=user_id,homework_id=homework_id).first().temporary_code

hwrepo = HomeworkRepository()