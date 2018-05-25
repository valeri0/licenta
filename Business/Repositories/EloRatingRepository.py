from Business.Repositories.UserRepository import UserRepository
from Business.Repositories.LessonRepository import LessonRepository
from Business.Repositories.ExerciseRepository import ExerciseRepository
from Data.Domain.UserExerciseDifficulty import UserExerciseDifficulty
from Data.Persistance.database import db_session
import elo, math


class EloRatingRepository:
    _user_repository = UserRepository()
    _lesson_repository = LessonRepository()
    _exercise_repository = ExerciseRepository()
    db_context = db_session

    def _get_elo_ratings(self, winner, loser):
        return elo.rate_1vs1(elo.Rating(winner), elo.Rating(loser))

    def _adjust_elo_rating_for_functions(self, winner, loser, test_case_factor):
        """
        This will adjust the elo rating of the entities when we are dealing with functions
        that need to be tested using different test cases.
        Example: in case an user does 9/10 tests, it wouldn't be fair if he totally loses,
        and the lesson wins. It must be adjusted
        using the ratio of test cases resolved as a proportion.

        :param winner: input elo of winner
        :param loser: input elo of loser
        :param test_case_factor: how many test cases there were completed
        :return:
        """
        default_elo = self._get_elo_ratings(winner, loser)

        new_elo_winner = default_elo[0]
        new_elo_loser = default_elo[1]

        default_gained_elo_points = math.fabs(winner - default_elo[0])

        new_elo_winner = winner + default_gained_elo_points - (default_gained_elo_points * test_case_factor)
        new_elo_loser = loser - default_gained_elo_points + (default_gained_elo_points * test_case_factor)

        return new_elo_winner, new_elo_winner

    def lesson_wins_over_user(self, lesson_id, test_case_factor):

        #TODO: check why the elo ratings are not being updated in the DB
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        lesson = self._lesson_repository.get_lesson_by_id(lesson_id)

        if not lesson.is_completed():

            lesson_old_elo = lesson.user_lesson_difficulty.elo_rating
            user_old_elo = user.elo_rating

            elo_lesson, elo_user = self._get_elo_ratings(lesson_old_elo, user_old_elo)

            if test_case_factor:
                elo_lesson, elo_user = self._adjust_elo_rating_for_functions(lesson_old_elo, user_old_elo,
                                                                             test_case_factor)

            user.elo_rating = elo_user
            lesson.user_lesson_difficulty.elo_rating = elo_lesson

            self.db_context.commit()

    def user_wins_over_lesson(self, lesson_id):
        #TODO: check why the elo ratings are not being updated in the DB

        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        lesson = self._lesson_repository.get_lesson_by_id(lesson_id)

        if not lesson.is_completed():
            elo_user, elo_lesson = self._get_elo_ratings(user.elo_rating, lesson.user_lesson_difficulty.elo_rating)

            user.elo_rating = elo_user
            lesson.user_lesson_difficulty.elo_rating = elo_lesson

            self._lesson_repository.mark_lesson_as_completed(lesson_id)

            self.db_context.commit()

    def exercise_wins_over_user(self, exercise_id, test_case_factor):
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        exercise = self._exercise_repository.get_exercise_by_id(exercise_id)
        #TODO: Implement mechanism persisting data into the database




    def user_wins_over_exercise(self, exercise_id):
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        exercise = self._exercise_repository.get_exercise_by_id(exercise_id)
        #TODO: Implement mechanism for persisting data into the database


        #
        #
        # if not lesson.is_completed():
        #
        #     lesson_old_elo = lesson.user_lesson_difficulty.elo_rating
        #     user_old_elo = user.elo_rating
        #
        #     elo_lesson, elo_user = self._get_elo_ratings(lesson_old_elo, user_old_elo)
        #
        #     if test_case_factor:
        #         elo_lesson, elo_user = self._adjust_elo_rating_for_functions(lesson_old_elo, user_old_elo,
        #                                                                      test_case_factor)
        #
        #     user.elo_rating = elo_user
        #     lesson.user_lesson_difficulty.elo_rating = elo_lesson
        #
        #     self.db_context.commit()
