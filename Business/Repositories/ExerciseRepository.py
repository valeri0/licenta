from Data.Persistance.database import *
from Data.Domain.Exercise import Exercise
from Data.Domain.UserExerciseDifficulty import UserExerciseDifficulty
from Data.Domain.ChapterExercise import ChapterExercise




class ExerciseRepository:
    _db_context = db_session

    def get_exercise_by_id(self,_id):
        return Exercise.query.filter_by(id=_id).first()

    def get_all_exercises(self):
        return Exercise.query.all()

    def get_all_exercises_for_user(self,user_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id).all()

    def get_all_exercises_from_chapter(self, chapter_id):
        return [self.get_exercise_by_id(cx.exercise_id) for cx in ChapterExercise.query.filter_by(chapter_id=chapter_id)]

    def all_exercises_are_completed_by_user(self, user_id):
        return all([x.is_completed for x in self.get_all_exercises_for_user(user_id)])

    def exercise_is_resolved_by_user(self,user_id,exercise_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id,exercise_id=exercise_id).first().completed




ex = ExerciseRepository()