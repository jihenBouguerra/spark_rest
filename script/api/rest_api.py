import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
jobs = [
    {'id': 0,
     'environment': 'Test',
     'data_type': 'DB_Small',
     'name': 'SL_CONTROL_UNIT_PLAN_V_csv',
     'source_name': 'Source'},
    {'id': 1,
     'environment': 'Test',
     'data_type': 'DB_Small',
     'name': 'PLAN_V_csv',
     'source_name': 'Source'},
    {'id': 2,
     'environment': 'Test',
     'data_type': 'DB_Small',
     'name': 'CONTROL_UNIT_PLAN_V_csv',
     'source_name': 'Source'},

]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Home page</h1>" \
           "<p>This site is a prototype API for ITAM Jobs.</p>"


@app.route('/api/jobs/all', methods=['GET'])
def api_all():
    return jsonify(jobs)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1>" \
           "<p>The resource could not be found.</p>", 404


@app.route('/api/jobs', methods=['GET'])
def get_job_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for job in jobs:
        if job['id'] == id:
            results.append(job)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


# call Function by
# curl -X POST -H "Content-type:application/json" --data "@data.json" http://localhost:5000/api/jobs/add

@app.route('/api/jobs/add', methods=['POST'])
def post_route():
    if request.method == 'POST':
        jobs_json = request.get_json()
        if jobs_json:
            for job in jobs_json:
                print(job)
            return "Request Processed.\n"
        else:
            return "Request Failed.\n"


app.run()
