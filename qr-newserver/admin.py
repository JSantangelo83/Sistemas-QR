from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound
import dbhelper as dbh

admin = Blueprint('admin', __name__,
                        template_folder='templates')

@admin.before_request
def before_anything():
    if not 'useremail' in session:
        return redirect(url_for('login'))
    if not dbh.is_admin(session['useremail']):
        return redirect(url_for('login'))    

@admin.route('/entity', strict_slashes=False)
def entity():
    return "chau"

@admin.route('/entity/<page>', strict_slashes=False)
def entity_mod(page):
    return "chau_mod"
