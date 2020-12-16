import sqlalchemy
import pandas as pd
import joblib
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
from sklearn.linear_model import LogisticRegression  

model = joblib.load('horse_model.sav')

Xtest = pd.DataFrame([0,3917,1400,5,13.53,21.59,23.94,23.58,13.53,35.12,59.06,82.64,10,8,2,2,1.5,8,13.85,21.59,23.86,24.62,9.7,3.7
])



engine = create_engine('postgresql://postgres:'+sqlkey+'@localhost:5432/horse_races')
connection = engine.connect()

filtered_sql = "select * from best_data_set where 1=1"
uniqueid_sql = "select * from uniqueids"


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


@app.route("/dataset", methods=["GET", "POST"])
@cross_origin()
def dataset():

    filtered_df = pd.read_sql(filtered_sql, connection)
    filtered_df_dictionary = filtered_df.to_dict('records')


    return jsonify(filtered_df_dictionary)

@app.route("/racegeneration", methods=["GET", "POST"])
@cross_origin()
def unique():

    unique_df = pd.read_sql(uniqueid_sql, connection)
    unique_df_dictionary = unique_df.to_dict('records')

    return jsonify(unique_df_dictionary)   

if __name__ == '__main__':
    app.run(debug=True)
