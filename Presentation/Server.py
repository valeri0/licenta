from flask import Flask, render_template, request
from Presentation.Controllers.Authentication import page
from flask_security import Security
from Business.Repositories.UserRepository import UserRepository
from Business.Services.UserService import UserService

user_repository = UserRepository()

user_service = UserService()

app = Flask(__name__)
app.register_blueprint(page)

security = Security(app, user_repository.get_user_datastore())


@app.before_first_request
def create_user():
    print("plm")
    user_service.create_user("myfirstmail@ccc.com","adsbnadsbsahuddsa21","user")


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('register.html')


@app.route('/', methods=['POST'])
def signUp():
    _email = request.form['input_email']
    _password = request.form['input_password']
    print(_email, _password)


if __name__ == '__main__':
    app.run()
