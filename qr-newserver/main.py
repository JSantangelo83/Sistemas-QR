from flask import Flask, render_template, request, make_response, session, flash, redirect, url_for
import os
import dbhelper as dbh
from datetime import timedelta
from auth import auth
from admin import admin

app = Flask(__name__, template_folder="templates")
#app.secret_key = os.urandom(12).hex()
app.secret_key = "comometrotaslasflexpedazodenoob123"
app.register_blueprint(auth)
app.register_blueprint(admin)


app.permanent_session_lifetime = timedelta(days=31)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    
    if 'useremail' in session:
        return redirect(url_for('auth.main'))
    
    if request.method == 'GET':
        return render_template("login.html")

    # POST
    email, password = request.form['email'].strip(), request.form['password'].strip()

    if not (email and password):
        error = "Por favor, comproba que el campo 'email' y/o el campo 'password' no se encuentren vacios"
        flash(error, 'error')
    else:
        user = dbh.get_user(email)
        if user:
            if user[1] == password:
                flash("Has iniciado sesion con exito!", 'success')
                session.permanent = True
                session["useremail"] = user[0]
                session["admin"] = user[2] 
                return redirect(url_for('auth.main'))
            else: error = "Contraseña incorrecta" # esto leakea
        else:
            error = "No se ha encontrado ninguna cuenta asociada a las credenciales ingresadas"
            flash(error, 'error')

    return redirect(url_for('login'))

# ------------------------------ ENDPOINTS ------------------------------
# /login    		[get,post]  -> permite el login de profesores (privilegios) y alumnos (usuarios comunes)

# requieren session (alumno o profesor):
# /         		[get]       -> principal page (useless!)
# /logout		[get]	    -> remueve session y redirect a /login

# requieren session y privilegios (profesor):
# /classes		[get]	    -> listado de clases
# /students		[get]	    -> listado de estudiantes
# /users		[get]	    -> listado de usuarios

                                ############
                                # API-LIKE #
                                ############
# /student   		[get, post] -> GET: devuelve alumno si hay id valido
# 			  	       POST: si es id valido, lo modifica; else crea alumno
# /student/delete	[post] ->      si es id valido, borra alumno

# /class    		[get, post] -> GET: devuelve clases si no recibe id_clase valido, else clase
#			 	       POST: modifica clase si es id valido; else crea clase
# /class/delete		[post] ->      si es id valido, borra clase

# /user    		[get, post] -> GET: devuelve users si no recibe id_user valido, else user
#			 	       POST: modifica user si es id valido; else crea user
# /user/delete		[post] ->      si es id valido, borra user
# -----------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
    print(app)
