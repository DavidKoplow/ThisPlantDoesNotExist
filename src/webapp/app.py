import requests
from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime, timedelta
import time
import json
import waitress
import os
from model import get_model

app = Flask('app') #create flask app 'app'


@app.route('/')  #"/" url mapped to show_predict_stock_form() function, which renders predictorform.html
def show_predict_stock_form():
    return render_template('predictorform.html')


@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        #write your function that loads the model
        model = get_model() #you can use pickle to load the trained model
        description = request.form['description']
        predicted_plant = "-------------------ppppppppplllllllllllaaaaaaaaannnnnnnnnntttttt---------" #model.predict(year)
        return render_template('resultsform.html', description=description, predicted_plant=predicted_plant)

app.run("localhost", "9999", debug=True)
