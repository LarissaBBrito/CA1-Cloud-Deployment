import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configuration
# Reads the DATABASE_URL environment variable set by App Engine or Cloud Build
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a simple model (The "User" table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Simple route to check if the app is running and the database is connected
@app.route('/')
def index():
    try:
        # Attempt to query the database to prove connection is working
        user_count = db.session.query(User).count()
        return f"Hello from App Engine! Database connection successful. Total users in DB: {user_count}"
    except Exception as e:
        # This error will show if the database is not connected or the table doesn't exist
        return f"Hello from App Engine! Database connection failed. Error: {e}"

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used in App Engine.
    app.run(host='127.0.0.1', port=8080, debug=True)
