from flask import Flask, render_template, request,flash,redirect, url_for,session
import sqlite3

from helper import login_required
app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    db = sqlite3.connect('recipes.db')
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
@login_required
def home():
    return render_template("layout.html")

# Register
@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":

        name = request.form.get("name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not name or not password or not confirm_password:
            flash("Please fill all Three column", 'error')
            return redirect(url_for("register"))
        
        if password != confirm_password:
            flash("Both password do not match", 'error')
            return redirect(url_for("register"))
        
        db = get_db_connection()
        
        users = db.execute("SELECT user FROM users").fetchall()

        for index,user in enumerate(users):
            users[index] = user[0]

        if name in users:
            flash("User Name Already exits", 'error')
            return redirect(url_for("register"))
        
        db.execute("INSERT INTO users(user,password) VALUES(?,?)", (name, password))
        db.commit()
        db.close()

        return render_template("login.html")
    else:
        return render_template("register.html")
    
# Login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        if not name or not password:
            flash("Please Fill Both Columns",'error')
            return redirect(url_for("login"))
        
        db = get_db_connection()

        users = db.execute("SELECT user from users").fetchall()
        for index,user in enumerate(users):
            users[index] = user[0]
        if name not in users:
            flash("Please Register first. This username does not exits", 'error')
            return redirect(url_for("login"))
        user_password = db.execute("SELECT password from users WHERE user = ?", [name]).fetchone()
        user_password = user_password[0]
        if password != user_password:
            flash("Incorrect Password", 'error')
            return redirect(url_for("login"))
        user_id = db.execute("SELECT id FROM users WHERE user = ?", [name]).fetchone()
        user_id = user_id[0]
        
        session["user_id"] = user_id

        db.close()
        return redirect("/")
    else:
        return render_template("login.html")

# Log out
@app.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)