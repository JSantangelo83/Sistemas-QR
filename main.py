from flask import Flask, render_template, request, make_response, session, flash, redirect, url_for
import os
import dbhelper as dbh

app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(12).hex()

@app.route("/")
def main():    
    if(session.get("token")):
        return render_template("index.html")
    else:
        return redirect('/login')


@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        print("RECIBI POST")
        email, password = request.form['email'].strip(), request.form['password'].strip()
        print(f"email {email} password {password}")

        if not (email and password):
            error = "Revisa que el email y/o el password no se encuentren vacios!"
            flash(error, 'error')
        else:
            user = dbh.getUser(email)
            if(user):
                if(user[1] == password):
                    flash("Has iniciado sesion con exito", 'success')
                    session["token"] = True
                    return redirect('/')
                else:
                    error = "Contraseña incorrecta!"
            else:
                error = "Ese usuario no existe!"
                
        return redirect(url_for('login'))

# endpoints
# /login    [get,post]  -> permite el login de admins y users
# /         [get]       -> 
# /entity   [post]      ->  
# /entity   [post]      ->  

# todas las rutas admin piden token
# adminlogin -- se loguea el profesor

# adminuser 
# postentidad-- if(id)modifica usuario else creas usuarios
# getid-- devuelve user
# deleteid-- deletea user

# adminclase
# post -- if(token) if(id) modifica clase else link else error
# get -- if(id) clase else clases

if __name__ == "__main__":
    app.run(debug=True)
