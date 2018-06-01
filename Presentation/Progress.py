from flask import Blueprint, render_template, request
from flask_login import current_user
from Business.Services.ExerciseService import ExerciseService
import json

progress = Blueprint('progress', __name__, template_folder='templates')


@progress.route("/progress", methods=['GET'])
def get_progress_page():
    return render_template("user_profile.html", user=current_user)
