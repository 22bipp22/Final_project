import random
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
# we may not need this -----  from keys import sqlkey
from sqlalchemy import and_
from flask_cors import cross_origin
from sklearn.linear_model import LogisticRegression 
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Length

# Added to create form -
class HorseForm(FlaskForm):
    winOdds = FloatField('Win Odds (1.0-100.0)', validators=[DataRequired()])
    placeOdds = FloatField('Place Odds (1.0-100.0)', validators=[DataRequired()])
    raceClass = SelectField('Race Class', choices=[0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 11.0, 12.0, 13.0], validators=[DataRequired()])
    distance = SelectField("Distance", choices=[1400,1600,1650,1800,2000,2200,2400], validators=[DataRequired()])
    lengthsBehind = FloatField('Lengths Behind Leader (0-999)', validators=[DataRequired()])
    submit = SubmitField('Generate a Race')


model = joblib.load('horse_time_model.sav')

Xtest = pd.DataFrame([0,3917,1400,5,13.53,21.59,23.94,23.58,13.53,35.12,59.06,82.64,10,8,2,2,1.5,8,13.85,21.59,23.86,24.62,9.7,3.7
])



engine = create_engine('postgresql://postgres:vxxvsttmphdruz:73d25ecb18a856e33e951d6426ab7ffa8131c83518b6a986faf1e35768255d87@ec2-54-159-107-189.compute-1.amazonaws.com:5432/d4lnindlr9uebh')
connection = engine.connect()

filtered_sql = "select * from best_ranked_data where 1=1"


app = Flask(__name__)

# Added to create form -
# Flask-WTF requires an encryption key - the string can be anything
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

#################################################
# Flask Routes
#################################################

@app.route("/", methods=["GET", "POST"])
@cross_origin()
def home():
    ## Added to create form -
    form = HorseForm()

    # If form data entered, populate fields from form
    if request.method == "POST":
        winOdds = form.winOdds.data
        placeOdds = form.placeOdds.data
        raceClass = form.raceClass.data 
        distance = form.distance.data 
        lengthsBehind = form.lengthsBehind.data
        print(f"HERE IT IS {winOdds}, {raceClass}, {distance}")
        # Call the function 'race' to run the mock race
        race(form)
    
    return render_template("index.html", form=form)



@app.route("/send", methods=["GET", "POST"])
@cross_origin()
def send():

    return render_template("page2.html")


@app.route("/dataset", methods=["GET", "POST"])
@cross_origin()
def dataset():

    filtered_df = pd.read_sql(filtered_sql, connection)
    filtered_df_dictionary = filtered_df.to_dict('records')
    print(f'this {filtered_df["horse_id"][0]}')

    return jsonify(filtered_df_dictionary)

# @app.route("/racegeneration", methods=["GET", "POST"])
# @cross_origin()
# def unique():

#     unique_df = pd.read_sql(uniqueid_sql, connection)
#     unique_df_dictionary = unique_df.to_dict('records')

#     return jsonify(unique_df_dictionary)

# Function to set up the mock race and run it through the ML model
def race(horse):  

    horse_df = pd.read_sql(filtered_sql, connection)

    winodds = horse.winOdds.data   
    placeodds = horse.placeOdds.data    
    raceclass = horse.raceClass.data
    distance = horse.distance.data    
    lengths = horse.lengthsBehind.data  

    race_df = pd.DataFrame ({
            "race_id": [2],
            "horse_id": [9999],
            "won": [0], 
            "distance": [distance],
            "race_class": [raceclass],
            "sec_time1": [23],
            "sec_time2": [24],
            "sec_time3": [23],
            "sec_time4": [24],
            "ldr_time1": [25],
            "ldr_time2": [28],
            "ldr_time3": [72],
            "ldr_time4": [95],
            "lengths_behind": [lengths],
            "behind_sec1": [3],
            "behind_sec2": [4],
            "behind_sec3": [7],
            "behind_sec4": [9],
            "time1": [25],
            "time2": [25],
            "time3": [25],
            "time4": [25],
            "finish_time": [0.00],
            "win_odds": [winodds],
            "place_odds": [placeodds]
        })

    horseNums = random.sample(range(4404), 13)
    print(f"horsenumbers {horseNums}")
    for num in horseNums: 
        row = horse_df.loc[horse_df['horse_id'] == num].iloc[0]
        df = pd.DataFrame ([[
            row.race_id,
            row.horse_id,
            row.won, 
            row.distance,
            row.race_class,
            row.sec_time1,
            row.sec_time2,
            row.sec_time3,
            row.sec_time4,
            row.ldr_time1,
            row.ldr_time2,
            row.ldr_time3,
            row.ldr_time4,
            row.lengths_behind,
            row.behind_sec1,
            row.behind_sec2,
            row.behind_sec3,
            row.behind_sec4,
            row.time1,
            row.time2,
            row.time3,
            row.time4,
            row.finish_time,
            row.win_odds,
            row.place_odds]], columns=race_df.columns)
        race_df = pd.concat([race_df, df])
        
        

    # print(f"one horse: {model.predict(horsearray)}") 
    print(f"race df {race_df}")

if __name__ == '__main__':
    app.run(debug=True)
