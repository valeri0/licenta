from flask import Blueprint, render_template

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

    return render_template("lesson.html",lesson=lesson)
