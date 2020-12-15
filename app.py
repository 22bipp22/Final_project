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
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Length

# Added to create form -
class HorseForm(FlaskForm):
    winOdds = FloatField('Win Odds', validators=[DataRequired()])
    secTime1 = FloatField('Section 1 Time', validators=[DataRequired()])
    distance = SelectField("Distance", choices=["1400", "2200"], validators=[DataRequired()])
    submit = SubmitField('Generate a Race')


model = joblib.load('horse_model.sav')

Xtest = pd.DataFrame([0,3917,1400,5,13.53,21.59,23.94,23.58,13.53,35.12,59.06,82.64,10,8,2,2,1.5,8,13.85,21.59,23.86,24.62,9.7,3.7
])



engine = create_engine('postgresql://postgres:'+sqlkey+'@localhost:5432/horse_races')
connection = engine.connect()

filtered_sql = "select * from best_data_set where 1=1"


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
    
    winOdds = form.winOdds.data
    secTime1 = form.secTime1.data 
    distance = form.distance.data 
    print(f"HERE IT IS {winOdds}, {secTime1}, {distance}")
    
    # return render_template("index.html")
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


    return jsonify(filtered_df_dictionary)

   

if __name__ == '__main__':
    app.run(debug=True)
