from Data.Persistance.database import *
from Data.Domain.Lesson import Lesson
from Data.Domain.UserLessonDifficulty import UserLessonDifficulty



class LessonRepository:
    _db_context = db_session


    def get_all_lessons(self):
        return Lesson.query.all()

    def get_lesson_by_id(self,lesson_id):
        return Lesson.query.filter_by(id=lesson_id).first()

    def get_lessons_ordered_by_id(self):
        return sorted(Lesson.query.all(),key = lambda a_lesson : a_lesson.id)

    def get_elo_rating_of_lesson_for_given_user(self,lesson_id,user_id):
        # TODO: Get elo rating of lesson for a specified user
        # return Lesson.query.filter_by(id=lesson_id,
        pass

    def mark_lesson_as_completed(self, lesson_id):
        lesson = self.get_lesson_by_id(lesson_id)
        lesson.user_lesson_difficulty.completed = 1
        self._db_context.commit()
        
        
    def assign_every_lesson_to_a_user(self,user_id):
        lessons = self.get_all_lessons()

        for lesson in lessons:
            user_difficulty = UserLessonDifficulty()

            user_difficulty.user_id = user_id
            user_difficulty.lesson_id = lesson.id
            user_difficulty.elo_rating = lesson.default_elo_rating

            self._db_context.add(user_difficulty)


        self._db_context.commit()



