from flask import render_template, Blueprint

from Business.Services.UserService import UserService
from Data.Utils.RegistrationForm import RegistrationForm
from Data.Utils.LoginForm import LoginForm

from flask_login import current_user, login_user,logout_user

from Data.Domain.User import User

page = Blueprint('auth', __name__, template_folder='templates')

user_service = UserService()


@page.route("/login", methods=['POST'])
def login():
    if current_user.is_authenticated:
        return render_template("dashboard.html")

    login_form = LoginForm()
    register_form = RegistrationForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is None:
            return render_template("register.html", login_form=login_form, register_form=register_form)

        else:
            flag = user.check_password(login_form.password.data)

            if flag is False:
                return render_template("register.html", login_form=login_form, register_form=register_form)

            else:
                login_user(user)
                return render_template("dashboard.html")

    else:
        return render_template("register.html", login_form=login_form, register_form=register_form)


@page.route("/register", methods=['POST'])
def register():
    if current_user.is_authenticated:
        return render_template("dashboard.html")

    login_form = LoginForm()
    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        if User.query.filter_by(email = register_form.email.data).first() is None:
            user_service.create_user(register_form.email.data,
                                     register_form.password.data,
                                     "user")
            return render_template("dashboard.html")
        else:
            return render_template("register.html", login_form=login_form, register_form=register_form)
    else:
        return render_template("register.html", login_form=login_form, register_form=register_form)


@page.route("/logout",methods=['GET'])
def logout():
    current_user.is_authenticated = False
    user_service.logout_user(current_user)

    logout_user()
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template("register.html", login_form=login_form, register_form=register_form)
