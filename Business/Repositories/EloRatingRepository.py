from Business.Repositories.UserRepository import UserRepository
from Business.Repositories.LessonRepository import LessonRepository
from Data.Persistance.database import db_session
import elo


class EloRatingRepository:
    _user_repository = UserRepository()
    _lesson_repository = LessonRepository()
    db_context = db_session


    def _get_elo_ratings(self, winner, loser):
        return elo.rate_1vs1(elo.Rating(winner), elo.Rating(loser))

    def _get_user_and_lesson_entities(self, lesson_id):
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        lesson = self._lesson_repository.get_lesson_by_id(lesson_id)

        return user, lesson

    def lesson_wins(self, lesson_id):

        user, lesson = self._get_user_and_lesson_entities(lesson_id)

        if not lesson.is_completed():

            elo_lesson,elo_user = self._get_elo_ratings(lesson.user_lesson_difficulty.elo_rating,user.elo_rating)

            user.elo_rating = elo_user
            lesson.user_lesson_difficulty.elo_rating = elo_lesson

            self.db_context.commit()

    def user_wins(self, lesson_id):



        user,lesson = self._get_user_and_lesson_entities(lesson_id)

        if not lesson.is_completed():

            elo_user,elo_lesson = self._get_elo_ratings(user.elo_rating,lesson.user_lesson_difficulty.elo_rating)

            user.elo_rating = elo_user
            lesson.user_lesson_difficulty.elo_rating = elo_lesson

            self._lesson_repository.mark_lesson_as_completed(lesson_id)

            self.db_context.commit()

