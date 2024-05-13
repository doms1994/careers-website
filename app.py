from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS=[
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'Location' : 'London',
        'salary' : '125.000 GBP'
    },
    {
        'id' : 2,
        'title' : 'Data Analyst',
        'Location' : 'London',
        'salary' : '125.000 GBP'
    },
    {
    'id' : 3,
    'title' : 'Tyre fitter',
    'Location' : 'London',
    'salary' : '125.000 GBP'
    },
    {
    'id' : 4,
    'title' : 'Full stack engineer',
    'Location' : 'London',
    'salary' : '125.999 GBP'
    }
]

@app.route("/")

def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/jobs")

def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
