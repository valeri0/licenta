from flask import Blueprint, render_template

courses = Blueprint('courses', __name__, template_folder='templates')

@courses.route("/courses",methods=['GET'])
def get_main_page():
    return render_template("lesson.html")

