from flask import Blueprint, render_template, request
import json

homeworks = Blueprint('homeworks', __name__, template_folder='templates')

@homeworks.route("/homeworks",methods=['GET'])
def get_homeworks():
    return render_template("homeworks.html")