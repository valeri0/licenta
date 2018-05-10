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

import json

from flask_login import current_user, login_user

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


@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("dashboard.html", name=current_user.get_display_name())

    register_form = RegistrationForm()
    login_form = LoginForm()
    return render_template("register.html", login_form=login_form, register_form=register_form)



if __name__ == '__main__':
    app.run(debug=True)
