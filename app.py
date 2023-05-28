from flask import Flask, request, render_template
import numpy as np
import requests
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
import requests
import json
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

file = open("pickle/model.pkl","rb")
gbc = pickle.load(file)
file.close()


app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")
     

@app.route("/detect",methods=["GET", "POST"])
def detect():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        return render_template('static/detect.html',xx =round(y_pro_non_phishing,2),url=url )
    return render_template("static/detect.html", xx =-1)

    

@app.route("/aboutus")
def aboutus():
    return render_template("static/aboutus.html")


if __name__ == "__main__":
    app.run(debug=True)