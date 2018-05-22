from Data.Domain.Chapter import Chapter
from Data.Persistance.database import db_session
from Business.Repositories.LessonRepository import LessonRepository
from Data.Domain import UserLessonDifficulty as uld, ChapterLesson as cl
from statistics import mean


class ChapterRepository:
    db_context = db_session
    _lesson_repository = LessonRepository()

    def get_all_chapters(self):
        return Chapter.query.all()

    def get_chapter_by_id(self, _id):
        return Chapter.query.filter_by(id=_id).first()

    def get_lessons_by_chapter_id(self, chapter_id):
        chapter = self.get_chapter_by_id(chapter_id)

        chapter_and_lessons = cl.ChapterLesson.query.all()

        lessons = []

        for chls in chapter_and_lessons:
            if chls.chapter_id == chapter.id:
                lessons.append(self._lesson_repository.get_lesson_by_id(chls.lesson_id))

        return lessons

    def get_lessons_grouped_by_chapter_for_view(self):
        '''

        :return: list of list of the form: [ [Chapter1, Lesson1,Lesson2],[Chapter2,Lesson1,Lesson2]]
        '''

        result = []

        chapters = Chapter.query.all()
        chapter_and_lessons = cl.ChapterLesson.query.all()

        for chapter in chapters:

            a_chapter_with_lessons = [chapter]

            for chls in chapter_and_lessons:
                if chls.chapter_id == chapter.id:
                    a_chapter_with_lessons.append(self._lesson_repository.get_lesson_by_id(chls.lesson_id))

            result.append(a_chapter_with_lessons)

        return result

    def get_max_of_elo_for_user(self, chapter_id, user_id):

        lessons = self.get_lessons_by_chapter_id(chapter_id)
        return max(
            [
                self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id,user_id) - lesson.default_elo_rating
                for lesson in lessons
                if lesson.default_elo_rating - self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id, user_id) < 0
             ]
        )

    def get_min_of_elo_for_user(self, chapter_id, user_id):
        lessons = self.get_lessons_by_chapter_id(chapter_id)
        return min(
            [
                self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id, user_id) - lesson.default_elo_rating
                for lesson in lessons
                if lesson.default_elo_rating - self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id, user_id) < 0
            ]
        )

    def get_mean_of_elo_for_user(self, chapter_id, user_id):
        lessons = self.get_lessons_by_chapter_id(chapter_id)
        return mean(
            [
                self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id,user_id) - lesson.default_elo_rating
                for lesson in lessons
                if lesson.default_elo_rating - self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id,user_id) < 0

             ]
        )




