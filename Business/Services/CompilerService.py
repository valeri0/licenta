from Business.Repositories.CompilerRepository import CompilerRepository
from Business.Repositories.EloRatingRepository import EloRatingRepository


def _format_output_error_message(message):
    return 'Error at: {}'.format(
        message.decode('utf-8')[len('  File "./script.py",'):])


class CompilerService:
    _compiler_repository = CompilerRepository()
    _elo_rating_repository = EloRatingRepository()

    def get_result_from_execution(self, source_code):

        result = self._compiler_repository.get_result_from_execution(source_code)

        # if the in stdout is empty that means the source code submitted has errors
        if not result[0] or not result[0].strip():
            return _format_output_error_message(result[1]), 500
        # else, the code has compiled and executed successfully
        else:
            return result[0].decode('utf-8'), 200

    def evaluate_submission(self, source_code, lesson_id):

        result = self.get_result_from_execution(source_code)

        if result[1] == 200:
            self._elo_rating_repository.user_wins(lesson_id)
        else:
            self._elo_rating_repository.lesson_wins(lesson_id)

        return result
