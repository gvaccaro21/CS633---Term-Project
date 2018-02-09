from flask import Flask, render_template, request, json
import db_connection

app = Flask(__name__)
 
"""The following Section contains all of the website routes"""

@app.route("/")
def index():
    """This the route for the index page"""
    return render_template('index.html')

@app.route("/measurements")
def measure():
    """This the route for the index page"""
    return render_template('measure.html')

@app.route("/generic")    
def generic():
    """This the route for the generic page"""
    return render_template('generic.html')

@app.route("/login") 
def login():
    """This the route for the login page"""
    return render_template('login.html')

@app.route('/saveMeasurements',methods=['POST'])
def saveMeasurements():
    _height = request.form['inputHeight']
    _weight = request.form['inputWeight']
    _bmi = request.form['inputBMI']
    #debug variables
    # _height = 1
    # _weight = 2
    # _bmi = 3

    if _height and _weight and _bmi:
        return json.dumps({'html':'<span>All fields good !!</span>'})
        myconn = db_connection.create_connection(test.db)
        myMeasurements = (2, 2, _height , _weight, _bmi)
        save_my_measurements(myconn, myMeasurements)
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run(debug=True)