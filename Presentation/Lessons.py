from flask import Blueprint, render_template,request
from Business.Services.ChapterService import ChapterService
from Business.Services.LessonService import LessonService
import json

lessons = Blueprint('courses', __name__, template_folder='templates')
_lesson_service = LessonService()
_chapter_service = ChapterService()


@lessons.route("/lessons", methods=['GET'])
def get_main_page():

    chapter_lessons = _chapter_service.get_lessons_by_chapter()

    return render_template("list_of_lessons.html",chapter_lessons = chapter_lessons)

@lessons.route("/lesson/<lesson_id>", methods=['GET'])
def get_lesson_by_id(lesson_id):
    lesson = _lesson_service.get_lesson_by_id(lesson_id)
    previous_lesson_id = _lesson_service.get_previous_lesson(lesson_id)
    next_lesson_id = _lesson_service.get_next_lesson(lesson_id)

    return render_template("lesson.html",lesson=lesson,previous_lesson_id=previous_lesson_id,next_lesson_id = next_lesson_id)


@lessons.route("/lesson/test", methods=['POST'])
def test_code():
    source_code = request.json['code']
    execution_response = _lesson_service.get_result_from_execution(source_code)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }
    return json.dumps(response), 200


@lessons.route("/lesson/submit", methods=['POST'])
def submit_code():
    source_code = request.json['code']
    lesson_id = request.json['id']

    execution_response = _lesson_service.evaluate_submission(source_code, lesson_id)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }
    return json.dumps(response), 200
