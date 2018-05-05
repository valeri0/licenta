from Business.Repositories.CompilerRepository import CompilerRepository


class CompilerService:
    _compiler_repository = CompilerRepository()

    def get_result_from_execution(self, source_code):

        result = self._compiler_repository.get_result_from_execution(source_code)

        # if the in stdout is empty that means the source code submitted has errors
        if not result[0] or not result[0].strip():
            return result[1], 500
        # else, the code has compiled and executed successfully
        else:
            return result[0], 200
