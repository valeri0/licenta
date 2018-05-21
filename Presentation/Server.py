from flask import Flask, render_template
from flask_security import Security
from flask_login import LoginManager

from Business.Repositories.UserRepository import UserRepository
from Business.Services.UserService import UserService
from Data.Utils.LoginForm import LoginForm
from Data.Utils.RegistrationForm import RegistrationForm
from Presentation.Authentication import auth
from Presentation.Lessons import lessons
from Presentation.Compiler import compiler
from flask_login import current_user

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import Data.Domain.User as user
from Presentation.AdminView.UserView import UserView

import Data.Domain.Chapter as chapter
from Presentation.AdminView.ChapterView import ChapterView

import Data.Domain.ChapterLesson as chapter_lesson
from Presentation.AdminView.ChapterLessonView import ChapterLessonView

import Data.Domain.ChapterExercise as chapter_exercise
from Presentation.AdminView.ChapterExerciseView import ChapterExerciseView

import Data.Domain.Lesson as lesson
from Presentation.AdminView.LessonView import LessonView

import Data.Domain.UserLessonDifficulty as user_lesson_difficulty
from Presentation.AdminView.UserLessonDifficultyView import UserLessonDifficultyView

import Data.Domain.Role as role
from Presentation.AdminView.RoleView import RoleView
app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(lessons)
app.register_blueprint(compiler)

app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = b"xxx"
app.config['SECURITY_PASSWORD_HASH'] = "sha512_crypt"
app.config['SECURITY_REGISTER_URL'] = '/create_account'
app.config['SECURITY_LOGIN_TEMPLATE'] = 'security/register.html'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.debug = True

login_manager = LoginManager()
login_manager.init_app(app)

user_repository = UserRepository()
user_service = UserService()
security = Security(app, user_repository.get_user_datastore())

admin = Admin(app, name="my app", template_mode="bootstrap3")
admin.add_view(UserView(user.User, user.db.db_session))

admin.add_view(RoleView(role.Role,role.db.db_session))
admin.add_view(UserLessonDifficultyView(user_lesson_difficulty.UserLessonDifficulty,user_lesson_difficulty.db.db_session))
admin.add_view(LessonView(lesson.Lesson,lesson.db.db_session))
admin.add_view(ChapterExerciseView(chapter_exercise.ChapterExercise,chapter_exercise.db.db_session))
admin.add_view(ChapterLessonView(chapter_lesson.ChapterLesson,chapter_lesson.db.db_session))
admin.add_view(ChapterView(chapter.Chapter,chapter.db.db_session))


@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("dashboard.html", name=current_user.get_display_name())

    register_form = RegistrationForm()
    login_form = LoginForm()
    return render_template("register.html", login_form=login_form, register_form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
