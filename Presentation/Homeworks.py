from flask import Blueprint, render_template, request
import json

from Business.Services.HomeworkService import HomeworkService

homeworks = Blueprint('homeworks', __name__, template_folder='templates')

_homework_service = HomeworkService()


@homeworks.route("/homeworks", methods=['GET'])
def get_list_of_homeworks():
    list_homeworks = _homework_service.get_incomplete_homeworks_for_user()
    return render_template("list_of_homeworks.html", homeworks=list_homeworks)


@homeworks.route("/homeworks/<homework_id>", methods=['GET'])
def get_homeworks(homework_id):
    homework = _homework_service.get_homework_by_id(homework_id)
    temporary_code = _homework_service.get_temporary_code_for_homework(homework_id)
    return render_template("homework.html", homework=homework, temporary_code=temporary_code)


@homeworks.route("/homeworks/test", methods=['POST'])
def test_homework():
    source_code = request.json['code']
    homework_id = request.json['id']

    execution_response = ('plm, e ok', 200)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }

    return json.dumps(response), 200


@homeworks.route("/homeworks/submit", methods=['POST'])
def submit_homework():
    source_code = request.json['code']
    homework_id = request.json['id']

    execution_response = ('plm, e ok', 200)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }

    return json.dumps(response), 200
