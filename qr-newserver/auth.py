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

@auth.route('/logout')
def logout():
    if 'useremail' in session:
        session.pop('useremail')

    wait_time = 3000
    seconds = wait_time / 1000
    redirect_url = url_for('login')

    return f"<html><body><p>Vas a ser redigirido al login en { int(seconds) } segundos...</p><script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}}, { wait_time });</script></body></html>"

@auth.route('/entity', strict_slashes=False)
def entity():
    return "chau"

@auth.route('/entity/<page>', strict_slashes=False)
def entity_mod(page):
    return "chau_mod"

# @auth.route('/<page>')
# def secondary(page):
#     try:
#         return render_template(f'index.html')
#     except TemplateNotFound:
#         abort(404)
