from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound

auth = Blueprint('auth', __name__,
                        template_folder='templates')

@auth.before_request
def before_anything():
    if not 'useremail' in session:
        return redirect(url_for('login'))
    

@auth.route('/')
def main():
    return render_template("index.html")
    
@auth.route('/<page>')
def secondary(page):
    try:
        return render_template(f'index.html')
    except TemplateNotFound:
        abort(404)
