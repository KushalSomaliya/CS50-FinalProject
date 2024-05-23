from flask import Flask, session, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure you have a secret key for session management

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
