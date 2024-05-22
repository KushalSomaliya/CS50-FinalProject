from flask import Flask, render_template, request,flash,redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    db = sqlite3.connect('recipes.db')
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def home():
    return redirect(url_for("register"))

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
        cursor = db.cursor()

        cursor.execute("SELECT user FROM users")
        users = cursor.fetchall()
        for index,user in enumerate(users):
            users[index] = user[0]
        if name in users:
            flash("User Name Already exits", 'error')
            return redirect(url_for("register"))

        db.execute("INSERT INTO users(user) VALUES(?)", name)
        db.commit()
        db.close()
        return render_template("login.html")
    else:
        return render_template("register.html")
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
    else:
        return render_template("login.html")    