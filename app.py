from flask import Flask, render_template, url_for, jsonify, request
from datetime import datetime

# Import data from your new data files
from data.python_data import python_data
from data.fullstack_data import fullstack_data
from data.aptitude_data import aptitude_data
from data.interview_questions_data import interview_questions_data
from data.problems_data import problems_data
from data.papers_data import papers_data

app = Flask(__name__)

# Combine domain data into a single dictionary for easier lookup in routes
# This maps the lowercase domain name to its imported data dictionary
domains_combined_data = {
    "python": python_data,
    "fullstack": fullstack_data,
    "aptitude": aptitude_data,
}

# All other data is directly imported

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/domains')
def domains():
    # Pass the combined domains_combined_data for the domains overview page
    return render_template('domains.html', domains=domains_combined_data)

@app.route('/domains/<domain_name>')
def domain_detail(domain_name):
    # Fetch specific domain data from the combined dictionary
    domain = domains_combined_data.get(domain_name.lower())
    if not domain:
        return render_template('404.html', message="Domain not found"), 404
    # This renders the specific HTML file for the domain (e.g., python.html)
    # which will then iterate through the domain's topics.
    return render_template(f'domains/{domain_name.lower()}.html', domain=domain)

@app.route('/problems')
def problems():
    return render_template('problems.html', problems=problems_data)

@app.route('/problems/<int:problem_id>')
def problem_detail(problem_id):
    problem = next((p for p in problems_data if p["id"] == problem_id), None)
    if not problem:
        return render_template('404.html', message="Problem not found"), 404
    # You would create a problem_detail.html if you want separate pages for each problem
    return render_template('problem_detail.html', problem=problem) # Placeholder

@app.route('/papers')
def papers():
    return render_template('papers.html', papers=papers_data)

@app.route('/interview-questions')
def interview_questions():
    return render_template('interview_questions.html', categories=interview_questions_data)

# API endpoints (can also fetch from imported data)
@app.route('/api/domains')
def api_domains():
    return jsonify(domains_combined_data)

@app.route('/api/problems')
def api_problems():
    return jsonify(problems_data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', message="The page you requested could not be found."), 404


if __name__ == '__main__':
    app.run(debug=True)