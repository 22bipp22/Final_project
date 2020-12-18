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
    session,
    redirect)
from keys import sqlkey
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



engine = create_engine('postgresql://postgres:'+sqlkey+'@localhost:5432/horse_races')
connection = engine.connect()

filtered_sql = "select * from best_ranked_data where 1=1"
uniqueid_sql = "select * from uniqueids"
fit_data = pd.read_sql(filtered_sql, connection)


app = Flask(__name__)

# Added to create form -
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

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
        df = race(form)
        session["data"] = df.to_json()
        return render_template("race.html")
    else: 
        return render_template("index.html", form=form)



@app.route("/send", methods=["GET", "POST"])
@cross_origin()
def send():

    return render_template("page2.html")


@app.route("/dataset", methods=["GET", "POST"])
@cross_origin()
def dataset():

    # filtered_df = pd.read_sql(filtered_sql, connection)
    # filtered_df_dictionary = filtered_df.to_dict('records')
    # print(f'this {filtered_df}')
    race_data = session.get('data')
    race_data = pd.read_json(race_data)
    print(f"race data {race_data}")
    filtered_df_dictionary = race_data.to_dict('records')
    print(f'this {filtered_df_dictionary}')

    return jsonify(filtered_df_dictionary)

# @app.route("/racegeneration", methods=["GET", "POST"])
# @cross_origin()
# def unique():

#     unique_df = pd.read_sql(uniqueid_sql, connection)
#     unique_df_dictionary = unique_df.to_dict('records')

#     return jsonify(unique_df_dictionary)

# Function to set up the mock race and run it through the ML model
def race(horse):  

    horse_df = pd.read_sql(uniqueid_sql, connection)

    winodds = horse.winOdds.data   
    placeodds = horse.placeOdds.data    
    raceclass = horse.raceClass.data
    distance = horse.distance.data    
    lengths = horse.lengthsBehind.data  

    race_df = pd.DataFrame ({
            "race_id": [320],
            "horse_id": [3992],
            "distance": [distance],
            "race_class": [raceclass],
            "sec_time1": [26.34],
            "sec_time2": [24.67],
            "sec_time3": [25.50],
            "sec_time4": [24.86],
            "ldr_time1": [26.34],
            "ldr_time2": [51.01],
            "ldr_time3": [76.51],
            "ldr_time4": [101.37],
            "lengths_behind": [lengths],
            "behind_sec1": [9.00],
            "behind_sec2": [8.75],
            "behind_sec3": [8.75],
            "behind_sec4": [8.50],
            "time1": [27.78],
            "time2": [24.63],
            "time3": [25.50],
            "time4": [24.82],
            "win_odds": [winodds],
            "place_odds": [placeodds]
        })

    horseNums = random.sample(range(4404), 13)
    print(f"horsenumbers {horseNums}")
    df = pd.DataFrame({})
    for num in horseNums:
        row = (horse_df.loc[horse_df['horse_id'] == num],)
        df = df.append(row)
    
    df = df.append(race_df)              
    
    from sklearn import preprocessing 
    scaler = preprocessing.MinMaxScaler()
    minmax_df = scaler.fit(fit_data.drop(columns=["won", "finish_time"]))
    random_race_scaled = scaler.transform(df)


    race_rank = (sorted(zip(model.predict(random_race_scaled),(df['horse_id'])), reverse=False))
    print(race_rank)
    print('-------------------------')
    print(f"The WINNER is Horse Number {race_rank[0][1]}")
    return df

if __name__ == '__main__':
    app.run(debug=True)
