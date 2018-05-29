from flask_login import current_user

from Data.Persistance.database import *
from Data.Domain.Exercise import Exercise
from Data.Domain.UserExerciseDifficulty import UserExerciseDifficulty
from Data.Domain.ChapterExercise import ChapterExercise


class ExerciseRepository:
    _db_context = db_session

    @staticmethod
    def get_exercise_by_id(_id):
        return Exercise.query.filter_by(id=_id).first()

    @staticmethod
    def get_all_exercises():
        return Exercise.query.all()

    @staticmethod
    def get_all_exercises_for_user(user_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id).all()

    def get_all_exercises_from_chapter(self, chapter_id):

        exercises_from_chapter = ChapterExercise.query.filter_by(chapter_id=chapter_id).all()
        list_of_exercises = []
        for exc in exercises_from_chapter:
            list_of_exercises.append(self.get_exercise_by_id(exc.exercise_id))

        return list_of_exercises

        # return [self.get_exercise_by_id(cx.exercise_id) for cx in exercises_from_chapter]

    def all_exercises_are_completed_by_user(self, user_id):
        return all([x.is_completed for x in self.get_all_exercises_for_user(user_id)])

    @staticmethod
    def exercise_is_resolved_by_user(user_id, exercise_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id, exercise_id=exercise_id).first().completed

    @staticmethod
    def exercise_has_been_tried_before_by_user(user_id, exercise_id):
        obj = UserExerciseDifficulty.query.filter_by(user_id=user_id, exercise_id=exercise_id).first()
        if obj:
            return obj
        return False

    @staticmethod
    def get_user_exercise_difficulty_for_user(exercise_id, user_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id, exercise_id=exercise_id).first()

    def create_user_exercise_difficulty_entry(self, exercise_id):
        user_id = current_user.id
        exercise = self.get_exercise_by_id(exercise_id)

        usr = UserExerciseDifficulty()
        usr.user_id = user_id
        usr.exercise_id = exercise_id
        usr.elo_rating = exercise.default_elo_rating
        usr.completed = False

        self._db_context.add(usr)
        self._db_context.commit()


ex = ExerciseRepository()

print(ex.get_all_exercises_from_chapter(2))
