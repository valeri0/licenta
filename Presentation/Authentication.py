from flask import  render_template, Blueprint

from Business.Services.UserService import UserService
from Data.Utils.RegistrationForm import RegistrationForm
from Data.Utils.LoginForm import LoginForm

page = Blueprint('auth', __name__, template_folder='templates')

user_service = UserService()

@page.route("/login", methods=['POST'])
def login():
    login_form = LoginForm()
    register_form = RegistrationForm()

    if login_form.validate_on_submit():
        print(login_form.__dict__)
        return render_template("dashboard.html")
    else:
        return render_template("register.html", login_form=login_form, register_form=register_form)


@page.route("/register", methods=['POST'])
def register():
    login_form = LoginForm()
    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        user_service.create_user(register_form.email,
                                 register_form.password,
                                 "user")
        return render_template("dashboard.html")
    else:
        return render_template("register.html", login_form=login_form, register_form=register_form)
