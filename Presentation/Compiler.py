import json

from flask import Blueprint, request

from Business.Services.CompilerService import CompilerService

compiler = Blueprint('compiler', __name__)

_compiler_service = CompilerService()


@compiler.route("/code/test", methods=['POST'])
def submit_code_for_test():
    source_code = request.json['code']

    execution_response = _compiler_service.get_result_from_execution(source_code)


    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }
    return json.dumps(response), 200
