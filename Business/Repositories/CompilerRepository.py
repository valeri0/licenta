import os
from subprocess import Popen, PIPE


class CompilerRepository:
    _compiler_aux_files_dir = os.path.join(os.path.dirname(__file__), 'CompilerAuxFiles')
    _filename = os.path.join(_compiler_aux_files_dir, 'script.py')

    def _write_in_file(self, source_code):
        with open(self._filename, "w") as write_file:
            write_file.write(source_code)

    def _run_in_docker(self, source_code):
        self._write_in_file(source_code)

        # building the docker container according to the Dockerfile
        os.system("docker build -t python-machine {}".format(self._compiler_aux_files_dir))

        # run the script.py in the docker container and provide the result
        proc = Popen('docker run python-machine', shell=True, stdout=PIPE, stderr=PIPE)

        # the result is a tuple (a,b) with:
        # a -> the stdout message
        # b -> the stderr message
        result_from_execution = proc.communicate()

        return result_from_execution

    def get_result_from_execution(self, source_code):
        return self._run_in_docker(source_code)
