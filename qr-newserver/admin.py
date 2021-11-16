from flask import Blueprint, render_template, abort, session, redirect, url_for, request, jsonify
from jinja2 import TemplateNotFound
import dbhelper as dbh

admin = Blueprint('admin', __name__,
                        template_folder='templates',
                  static_url_path="/",
                  static_folder="static")

@admin.before_request
def before_anything():
    if not 'useremail' in session:
        return redirect(url_for('login'))
    if not dbh.is_admin(session['useremail']):
        return redirect(url_for('login'))    

@admin.route('/users', strict_slashes=False, methods=["GET"])
def users():
    return render_template("entities.html", email=session['useremail'], admin=True, title="Usuarios", name="users")

@admin.route('/classes', strict_slashes=False, methods=["GET"])
def classes():
    return render_template("entities.html", email=session['useremail'], admin=True, title="Clases", name="classes")

@admin.route('/professors', strict_slashes=False, methods=["GET"])
def professors():
    return render_template("entities.html", email=session['useremail'], admin=True, title="Profesores", name="professors")

@admin.route('/students', strict_slashes=False, methods=["GET"])
def students():
    return render_template("entities.html", email=session['useremail'], admin=True, title="Estudiantes", name="students")

@admin.route('/user', strict_slashes=False, methods=["GET", "POST"])
def user():
    if request.method == "GET":
        gid = request.args.get('id') or -1
        result = dbh.get_user(gid)
        if gid == -1:
            users = dbh.get_users()
            return jsonify(users)
        return jsonify(result)
    
    # POST    
    return "chau"

@admin.route('/class', strict_slashes=False, methods=["GET", "POST"])
def c_class():
    if request.method == "GET":
        gid = request.args.get('id') or -1
        result = dbh.get_class(gid)
        if gid == -1:
            users = dbh.get_classes()
            return jsonify(users)
        return jsonify(result)
    
    # POST    
    return "chau"

@admin.route('/professor', strict_slashes=False, methods=["GET", "POST"])
def professor():
    if request.method == "GET":
        gid = request.args.get('id') or -1
        result = dbh.get_professor(gid)
        if gid == -1:
            users = dbh.get_professors()
            return jsonify(users)
        return jsonify(result)
    
    # POST    
    return "chau"

@admin.route('/student', strict_slashes=False, methods=["GET", "POST"])
def student():
    if request.method == "GET":
        gid = request.args.get('id') or -1
        result = dbh.get_student(gid)
        if gid == -1:
            users = dbh.get_students()
            return jsonify(users)
        return jsonify(result)
    
    # POST    
    return "chau"
