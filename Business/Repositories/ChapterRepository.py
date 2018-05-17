from Data.Domain.Chapter import ChapterLesson, Chapter, ChapterExercise
from Data.Persistance.database import db_session
from Business.Repositories.LessonRepository import LessonRepository


class ChapterRepository:
    db_context = db_session
    _lesson_repository = LessonRepository()

    def get_all_chapters(self):
        return Chapter.query.all()

    def get_chapter_by_id(self, _id):
        return Chapter.query.filter_by(id=_id).first()

    def get_lessons_by_chapter(self):
        '''

        :return: list of list of the form: [ [Chapter1, Lesson1,Lesson2],[Chapter2,Lesson1,Lesson2]]
        '''

        result = []

        chapters = Chapter.query.all()
        chapter_and_lessons = ChapterLesson.query.all()

        for chapter in chapters:

            a_chapter_with_lessons = [chapter]

            for chls in chapter_and_lessons:
                if chls.chapter_id == chapter.id:
                    a_chapter_with_lessons.append(self._lesson_repository.get_lesson_by_id(chls.lesson_id))

            result.append(a_chapter_with_lessons)

        return result



chr = ChapterRepository()

chr.get_lessons_by_chapter()
