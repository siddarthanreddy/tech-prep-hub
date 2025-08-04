from flask import Flask, render_template, request, redirect, url_for, session, g, abort
import sqlite3 # Re-added: for database management
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash # Re-added: for secure password handling
from functools import wraps # Re-added: for login_required decorator


# --- CORRECTED IMPORTS BASED ON YOUR FOLDER STRUCTURE (all from 'data' directory) ---
from data.python_data import python_data as python_roadmap
# from data.dsa_data import dsa_data as dsa_roadmap # Uncomment and define if you have DSA roadmap
# from data.logicalreasoning_data import logicalreasoning_data as reasoning_roadmap
from data.aptitude_data import aptitude_data as aptitude_roadmap
from data.fullstack_data import fullstack_data as fullstack_roadmap
from data.dataanalyst_data import dataanalyst_data as analyst_roadmap
from data.papers_data import papers_data as papers_content # Assuming papers_data.py exists and has 'papers_data'
from data.problems_data import problems_data as problems_content # Assuming problems_data.py exists and has 'problems_data'
from data.interview_questions_data import interview_questions_data as interview_questions_content # Corrected import for interview questions
# --- IMPORTS FOR ALL NEW DOMAINS ---
from data.cybersecurity_data import cybersecurity_data as cybersecurity_roadmap
from data.java_data import java_data as java_roadmap
from data.devops_data import devops_data as devops_roadmap
from data.aws_data import aws_data as aws_roadmap
from data.machine_learning_data import machine_learning_data as ml_roadmap


app = Flask(__name__)
# IMPORTANT: Change this to a strong, random key in production!
# You can generate one using: import os; os.urandom(24)
app.secret_key = 'your_super_secret_and_random_key_here_please_change_me_in_production'

DATABASE = 'database.db'

# --- Database Helper Functions (Re-added) ---
def get_db():
    """Connects to the specific database."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row # This allows you to access columns by name
    return db

@app.teardown_appcontext
def close_connection(exception):
    """Closes the database connection at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Initializes the database schema."""
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL -- This will store the HASHED password
            )
        ''')
        db.commit()
        print("Database initialized or already exists.")

# Call init_db once when the application starts
# This will ensure the 'users' table exists
with app.app_context():
    init_db()


# --- Context Processor for current_year and user_info (Re-added user info) ---
# This makes these variables available in all templates
@app.context_processor
def inject_global_data():
    user_logged_in = None
    user_name = None
    if 'user_email' in session:
        user_logged_in = session['user_email']
        user_name = session.get('user_name', user_logged_in) # Get name if available, else email
    return dict(current_year=datetime.now().year, user_logged_in=user_logged_in, user_name=user_name)


# --- Login Required Decorator (Re-added and ready to use) ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            # Redirect to login page, potentially with a 'next' parameter
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# --- Routes ---

# Public Home Page (Your "Ignite Your Tech Journey" page)
@app.route('/')
def index(): # This function handles the root URL and renders index.html
    return render_template('index.html')


# Login Route (Re-added)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_email' in session:
        return redirect(url_for('index')) # If already logged in, redirect to home (index)

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT id, name, email, password FROM users WHERE email = ?", (email,))
        user = cur.fetchone()

        if user:
            if check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['user_email'] = user['email']
                session['user_name'] = user['name']
                # Redirect to the 'next' page if provided, otherwise to 'index' (home)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('index'))
            else:
                return render_template('login.html', error="Invalid email or password.")
        else:
            return render_template('login.html', error="Invalid email or password.")

    return render_template('login.html')

# Signup Route (Re-added)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user_email' in session:
        return redirect(url_for('index')) # If already logged in, redirect to home (index)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        plain_text_password = request.form['password']

        hashed_password = generate_password_hash(plain_text_password)

        db = get_db()
        cur = db.cursor()

        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = cur.fetchone()

        if existing_user:
            return render_template('register.html', error="Email already exists. Please login or use a different email.")

        try:
            cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                        (name, email, hashed_password))
            db.commit()
            return redirect(url_for('login')) # Redirect to login after successful signup
        except sqlite3.Error as e:
            db.rollback()
            return render_template('register.html', error=f"An error occurred during signup: {e}. Please try again.")

    return render_template('register.html')

# Logout Route (Re-added)
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    session.pop('user_name', None)
    return redirect(url_for('index')) # Redirect to public home page after logout


# --- All content pages now require login ---
@app.route('/domains')
@login_required # Requires login
def domains():
    return render_template('domains.html')


@app.route('/roadmap/<name>') # Handles individual domain pages (e.g., /roadmap/python)
@login_required # Requires login
def roadmap(name):
    roadmap_data = {
        'python': python_roadmap,
        # 'dsa': dsa_roadmap, # Uncomment if defined and imported from data/dsa_data.py
        'aptitude': aptitude_roadmap,
        # 'logicalreasoning': reasoning_roadmap, # Uncomment if defined and imported from data/logicalreasoning_data.py
        'fullstack': fullstack_roadmap,
        'dataanalyst': analyst_roadmap,
        'cybersecurity': cybersecurity_roadmap, # Re-added new domain
        'java': java_roadmap, # Re-added new domain
        'devops': devops_roadmap, # Re-added new domain
        'aws': aws_roadmap, # Re-added new domain
        'machinelearning': ml_roadmap, # Re-added new domain
    }

    data = roadmap_data.get(name.lower())

    if data:
        return render_template(f'domains/{name}.html', roadmap=data)
    else:
        abort(404)

# --- PROBLEMS PAGE ---
@app.route('/problems')
@login_required # Requires login
def problems():
    return render_template('problems.html', problems=problems_content)

# --- PREVIOUS PAPERS PAGE ---
@app.route('/papers')
@login_required # Requires login
def papers():
    return render_template('papers.html', papers=papers_content)


# --- INTERVIEW QUESTIONS PAGE ---
@app.route('/interview') # Endpoint name remains 'interview'
@login_required # Requires login
def interview():
    return render_template('interview_questions.html', categories=interview_questions_content)


# --- Error Handlers ---
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', message="The page you are looking for does not exist."), 404


# Entry point
if __name__ == '__main__':
    app.run(debug=True)