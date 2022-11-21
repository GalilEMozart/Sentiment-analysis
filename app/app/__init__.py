# app/__init__.py

from flask_api import FlaskAPI
from scipy.sparse import data
from instance.config import app_config
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import json
import numpy as np
from scipy.sparse import hstack


def length_review(text):
    return len(text) 

def lenght_title(text):
    return len(text)


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')


    def abord_if_bad_request(data):
        #not(eval(data["stars"]) in range(1,6)) or\
            #type(eval(data["stars"])) != int or \
            
        if len(data.keys()) != 3 or \
            not( "review" in data.keys() and "title" in data.keys() and "stars" in data.keys()):
            
            res = {
                'error': 'Your request is not correct! Please read our documentation'
            }
            
            return True,json.dumps(res)
        return False, ''


    @app.route('/predict/', methods=['POST', 'GET'])
    def predict():

        content = request.get_json(force=True)
        
        res,send=abord_if_bad_request(content)
        if(res):return send
        
        review = content['review']
        title = content['title']
        stars = int(content['stars'])

        other_features = np.array([length_review(review),lenght_title(title),stars]).reshape((1,-1))


        #load model and tfv        
        model = pickle.load(open('model/random_model.model', 'rb'))
        vectorizer = pickle.load(open('model/tfidf.pickle', 'rb'))

        data = vectorizer.transform([review])

        data = hstack([data,other_features])

        predict = int(model.predict(data)[0])
        score = float(model.predict_proba(data)[0][predict])

        pred = {
                'prediction':predict,
                'score': score 
                }

        
        return json.dumps(pred)

    return app