from flask import Blueprint, request, url_for, redirect, render_template
blueprint1 = Blueprint('blueprint1', __name__, template_folder="templates/blueprint1")

@blueprint1.route("/")
def home():
    return render_template('index.html')

@blueprint1.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404