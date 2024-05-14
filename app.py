from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'description': 'Work on Google Search'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'company': 'Facebook',
        'location': 'Menlo Park, CA',
        'description': 'Work on Facebook News Feed'
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'company': 'Amazon',
        'location': 'Seattle, WA',
        'description': 'Work on Amazon Web Services'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)