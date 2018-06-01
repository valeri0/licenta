from Business.Repositories.LessonRepository import LessonRepository
from Business.Services.CompilerService import CompilerService


class LessonService:
    _lesson_repository = LessonRepository()
    _compiler_service = CompilerService()

    def get_all_lessons(self):
        return self._lesson_repository.get_all_lessons()

    def get_lesson_by_id(self, lesson_id):
        return self._lesson_repository.get_lesson_by_id(lesson_id)

    def get_lessons_ordered_by_id(self):
        return self._lesson_repository.get_lessons_ordered_by_id()

    def evaluate_submission(self, source_code, source_id):
        return  self._compiler_service.evaluate_submission(source_code,source_id)

    def get_result_from_execution(self, source_code):
        return self._compiler_service.get_result_from_execution(source_code)

    def get_next_lesson(self,current_lesson_id):
        return self._lesson_repository.get_next_lesson(current_lesson_id)

    def get_previous_lesson(self,current_lesson_id):
        return self._lesson_repository.get_previous_lesson(current_lesson_id)
