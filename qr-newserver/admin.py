from flask import Blueprint, render_template, abort, session, redirect, url_for, request, jsonify
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

@admin.route('/users', strict_slashes=False, methods=["GET"])
def users():
    return "Estos son los users: (ninguno) !!"

@admin.route('/classes', strict_slashes=False, methods=["GET"])
def classes():
    return "Estas son las classes: (ninguna) !!"

@admin.route('/professors', strict_slashes=False, methods=["GET"])
def professors():
    return "Estos son los professors: (ninguno) !!"

@admin.route('/students', strict_slashes=False, methods=["GET"])
def students():
    return "Estos son los students: (ninguno) !!"

@admin.route('/user', strict_slashes=False, methods=["GET", "POST"])
def user():
    if request.method == "GET":
        gid = request.args.get('id') or -1
        result = dbh.get_user(gid)
        if gid == -1 or not result:
            users = dbh.get_users()
            return jsonify(users)
        return jsonify(result)
        
        
    
    # POST    
    return "chau"

