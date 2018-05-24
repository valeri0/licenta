from flask import Blueprint, render_template
from flask_login import current_user
from Business.Services.ExerciseService import ExerciseService
import json

exercises = Blueprint('exercises', __name__, template_folder='templates')
_exercise_service = ExerciseService()


@exercises.route("/exercise/", methods=['GET'])
def suggest_exercise():
    exercise = _exercise_service.suggest_exercise_for_user(current_user.id)

    return render_template("exercise.html", exercise=exercise)
