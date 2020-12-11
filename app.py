import json
from flask import (
    Flask, 
    jsonify, 
    render_template, 
    request, 
    redirect)


app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    
    return render_template("index.html");



@app.route("/send", methods=["GET", "POST"])
def send():

    return render_template("page2.html")

@app.route("/button", methods=["GET", "POST"])
def button():

    return render_template("page2.html")

    
    

if __name__ == '__main__':
    app.run(debug=True)
