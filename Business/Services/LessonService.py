from Business.Repositories.LessonRepository import LessonRepository


class LessonService:
    _lesson_repository = LessonRepository()

    def get_lesson_by_id(self, lesson_id):
        return self._lesson_repository.get_lesson_by_id(lesson_id)

    def get_lessons_ordered_by_id(self):
        return self._lesson_repository.get_lessons_ordered_by_id()
