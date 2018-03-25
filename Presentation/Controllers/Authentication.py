from flask import Blueprint,render_template

page = Blueprint('yourname',__name__,template_folder='templates')

@page.route("/yourname")
def do():
    print('aicia sunt')
    return render_template("dashboard.html")