from Business.Repositories.CompilerRepository import CompilerRepository


class CompilerService:
    _compiler_repository = CompilerRepository()

    def _format_output_error_message(self, message):
        return 'Error at: {}'.format(
            message.decode('utf-8')[len('  File "./script.py",'):])

    def get_result_from_execution(self, source_code):

        result = self._compiler_repository.get_result_from_execution(source_code)

        # if the in stdout is empty that means the source code submitted has errors
        if not result[0] or not result[0].strip():
            return self._format_output_error_message(result[1]), 500
        # else, the code has compiled and executed successfully
        else:
            return result[0].decode('utf-8'), 200
