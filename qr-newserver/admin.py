from flask import Blueprint, render_template, abort, session, redirect, url_for, request, jsonify
from jinja2 import TemplateNotFound
import dbhelper as dbh

admin = Blueprint('admin', __name__,
                        template_folder='templates',
                  static_url_path="/",
                  static_folder="static")

@admin.before_request
def before_anything():
    if request.endpoint != "admin.pk":
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
    return render_template("entities.html", email=session['useremail'], admin=True, title="Docentes", name="professors")

@admin.route('/students', strict_slashes=False, methods=["GET"])
def students():
    return render_template("entities.html", email=session['useremail'], admin=True, title="Estudiantes", name="students")

@admin.route('/pk', strict_slashes=False, methods=["GET"])
def pk():
    name = request.args.get('name')
    return {"pk": dbh.get_primary_key_field(name)}

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
    success = 0
    try:
        request.json["Admin"] = bool(int(request.json["Admin"]))
        success = 1
    except:
        return jsonify({"success": 0})        

    if dbh.user_exists(request.json["pk"]):
        print("ya existe")
        if "create" in request.json:
            if request.json["create"]: return jsonify({"success": 0})
            del request.json["create"]

        try:
            dbh.update_user(request.json)
            success &= 1
        except Exception as e:
            print(e)
            success &= 0

        return jsonify({"success": success})

    print("nuevo")
    if not "create" in request.json: return jsonify({"success": 0})
    if request.json["create"] != 1: return jsonify({"success": 0})
    del request.json["create"]
    
    try:
        dbh.insert_full("usuarios", request.json)
        success = 1
    except: success &= 0
        
    return jsonify({"success": success})

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
    success = 0
    try:
        request.json["Id"] = int(request.json["Id"])
        request.json["pk"] = int(request.json["pk"])
        success = 1
    except:
        print("fallo al parsear")
        return jsonify({"success": success})

    if dbh.class_exists(request.json["pk"]):
        if "create" in request.json:
            if request.json["create"]: return jsonify({"success": 0})
            del request.json["create"]
        
        try:
            dbh.update_class(request.json)
            success &= 1
        except: success &= 0
        
        return jsonify({"success": success})

    if not "create" in request.json: return jsonify({"success": 0})
    if request.json["create"] != 1: return jsonify({"success": 0})
    del request.json["create"]
    
    try:
        dbh.insert_full("modulos", request.json)
        success = 1
    except Exception as e:
        print(e)
        success &= 0
        
    return jsonify({"success": success})

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
    success = 0
    try:
        request.json["Dni"] = int(request.json["Dni"])
        request.json["pk"] = int(request.json["pk"])
        success = 1
    except:
        return jsonify({"success": 0})        

    if dbh.professor_exists(request.json["pk"]):
        print("ya existe")
        if "create" in request.json:
            if request.json["create"]: return jsonify({"success": 0})
            del request.json["create"]

        try:
            dbh.update_professor(request.json)
            success &= 1
        except Exception as e:
            print(e)
            success &= 0

        return jsonify({"success": success})

    print("nuevo")
    if not "create" in request.json: return jsonify({"success": 0})
    if request.json["create"] != 1: return jsonify({"success": 0})
    del request.json["create"]
    
    try:
        dbh.insert_full("docentes", request.json)
        success = 1
    except: success &= 0
        
    return jsonify({"success": success})

@admin.route('/user/delete', strict_slashes=False, methods=["POST"])
def user_delete():
    pk = request.json["pk"]
    if not isinstance(pk, list): pk = [pk]
    success = 0
    try:
        dbh.delete_user(pk)
        success = 1
    except: pass
    return {"success": success}

@admin.route('/class/delete', strict_slashes=False, methods=["POST"])
def class_delete():
    pk = request.json["pk"]
    if not isinstance(pk, list): pk = [pk]
    success = 0
    try:
        dbh.delete_class(pk)
        success = 1
    except: pass
    return {"success": success}

@admin.route('/student/delete', strict_slashes=False, methods=["POST"])
def student_delete():
    pk = request.json["pk"]
    if not isinstance(pk, list): pk = [pk]
    success = 0
    try:
        dbh.delete_student(pk)
        success = 1
    except: pass
    return {"success": success}

@admin.route('/professor/delete', strict_slashes=False, methods=["POST"])
def professor_delete():
    pk = request.json["pk"]
    if not isinstance(pk, list): pk = [pk]
    success = 0
    try:
        dbh.delete_professor(pk)
        success = 1
    except: pass
    return {"success": success}

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
    success = 0
    try:
        request.json["Dni"] = int(request.json["Dni"])
        request.json["pk"] = int(request.json["pk"])
        success = 1
    except:
        return jsonify({"success": 0})        

    if dbh.student_exists(request.json["pk"]):
        print("ya existe")
        if "create" in request.json:
            if request.json["create"]: return jsonify({"success": 0})
            del request.json["create"]

        try:
            dbh.update_student(request.json)
            success &= 1
        except Exception as e:
            print(e)
            success &= 0

        return jsonify({"success": success})

    print("nuevo")
    if not "create" in request.json: return jsonify({"success": 0})
    if request.json["create"] != 1: return jsonify({"success": 0})
    del request.json["create"]
    
    try:
        dbh.insert_full("alumnos", request.json)
        success = 1
    except: success &= 0
        
    return jsonify({"success": success})
