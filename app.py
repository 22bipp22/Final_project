import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from keys import sqlkey
from sqlalchemy import and_
from flask_cors import cross_origin




engine = create_engine('postgresql://postgres:'+sqlkey+'@localhost:5432/horse_races')
connection = engine.connect()

filtered_sql = "select * from best_data_set where 1=1"


app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
@cross_origin()
def home():
    
    return render_template("index.html");



@app.route("/send", methods=["GET", "POST"])
@cross_origin()
def send():

    return render_template("page2.html")

@app.route("/button", methods=["GET", "POST"])
@cross_origin()
def button():

    f = open('output/complete.json')
    
    data = json.loads(f.read())

    f.close()

    return jsonify(data)

@app.route("/dataset", methods=["GET", "POST"])
@cross_origin()
def dataset():

    filtered_df = pd.read_sql(filtered_sql, connection)
    filtered_df_dictionary = filtered_df.to_dict('records')

    return jsonify(filtered_df_dictionary)

   

if __name__ == '__main__':
    app.run(debug=True)
