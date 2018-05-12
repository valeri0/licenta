from Data.Persistance.database import *
from Data.Domain.Lesson import Lesson


class LessonRepository:
    _db_context = db_session

    def get_lesson_by_id(self,lesson_id):
        return Lesson.query.filter_by(id=lesson_id).first()

    def get_lessons_ordered_by_id(self):
        return sorted(Lesson.query.all(),key = lambda a_lesson : a_lesson.id)

    def get_elo_rating_of_lesson_for_given_user(self,lesson_id,user_id):
        # TODO: Get elo rating of lesson for a specified user
        # return Lesson.query.filter_by(id=lesson_id,
        pass

