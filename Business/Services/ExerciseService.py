from Business.Repositories.ExerciseRepository import ExerciseRepository
from Business.Repositories.ChapterRepository import ChapterRepository
from Business.Repositories.UserRepository import UserRepository
import random, elo


class ExerciseService:
    _exercise_repository = ExerciseRepository()
    _chapter_repository = ChapterRepository()
    _user_repository = UserRepository()

    def suggest_exercise_for_user(self, user_id):
        # if all the lessons are completed, then a random exercise from all the ones will be generated
        if self._exercise_repository.all_exercises_are_completed_by_user(user_id):
            all_exercises_id = [ex.id for ex in self._exercise_repository.get_all_exercises()]
            return self._exercise_repository.get_exercise_by_id(random.choice(all_exercises_id))

        # else, we will generate the possible exercises that the user should resolve, based on his progress

        all_chapters = self._chapter_repository.get_all_chapters()
        chapters_with_criteria = []

        for chapter in all_chapters:
            chapter_id = chapter.id

            # first we will take the exercises from the chapter which has the mean elo defined by lessons lesser than the others
            # we'll try it with the min or max or other selection method if we see it's not efficient

            mean_elo_chapter = self._chapter_repository.get_mean_of_elo_for_user(chapter_id, user_id)
            # min_elo_chapter = self._chapter_repository.get_min_of_elo_for_user(chapter_id, user_id)
            # max_elo_chapter = self._chapter_repository.get_max_of_elo_for_user(chapter_id, user_id)


            chapters_with_criteria.append(
                (chapter_id, mean_elo_chapter)
            )

        # sort ascending the chapters based on the criteria
        chapters_with_criteria.sort(key=lambda tup: tup[1])

        # TODO: find a treshold which will ignore the chapters, meaning that the user did well on that chapter and is not necessary for exercises
        treshold = 1000

        chapter_id = min(chapters_with_criteria, key=lambda tup: tup[1] < treshold)

        all_exercises = self._exercise_repository.get_all_exercises_from_chapter(chapter_id)

        best_chance_to_win = (0, float('-inf'))
        user_elo = self._user_repository.get_user_by_id(user_id).elo_rating

        for exercise in all_exercises:
            chances_for_user_to_do_the_exercise = elo.quality_1vs1(user_elo, exercise.default_elo_rating)
            if chances_for_user_to_do_the_exercise > best_chance_to_win[1]:
                best_chance_to_win = (exercise.id, chances_for_user_to_do_the_exercise)

        return self._exercise_repository.get_exercise_by_id(best_chance_to_win[0])
