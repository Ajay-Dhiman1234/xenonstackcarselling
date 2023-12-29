from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite database configuration
DB_NAME = 'users.db'

@app.route('/')
def index():
    return render_template("C:\Users\ajay dhiman\Desktop\Project1\carselling.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Connect to SQLite database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Check if the user exists in the database
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        # Successful login, redirect to some page
        return redirect(url_for('dashboard'))
    else:
        # Failed login, redirect back to the login page
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
    # Create a SQLite database and table if not exists
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
    conn.commit()
    conn.close()

    # Run the Flask app
    app.run(debug=True)
