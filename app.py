from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app=Flask(__name__)

@app.route('/',methods=['GET'])##Route to Display Home Page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET']) ## Route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" ## We can return any string here.


@app.route('/predict',methods=['POST','GET']) #Route to show the predictions in a web UI