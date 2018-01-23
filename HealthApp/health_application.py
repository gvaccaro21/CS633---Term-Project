from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/test")
def hello():
    one = "Hello"
    two = "World"
    return one + " " + two
 
@app.route("/")
def home():
 	return render_template('index.html')

@app.route("/generic")
def generic():
    return render_template('generic.html')

if __name__ == "__main__":
    app.run()