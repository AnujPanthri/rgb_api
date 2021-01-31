# -*- coding: utf-8 -*-
## Importing Libraries
import numpy as np
import flask
from flask import request, jsonify
# Importing Tensorflow
import tensorflow as tf

#print(tf.__version__)

"""## Loading Trained Model"""
# Recreate the exact same model, including its weights and the optimizer
model = tf.keras.models.load_model('colormodel_trained.h5') 

"""## Initializing Color Classes for Prediction"""

# Mapping the Color Index with the respective 11 Classes (More Explained in RGB Color Classifier: Part 1)
color_dict={
    0 : 'Red',
    1 : 'Green',
    2 : 'Blue',
    3 : 'Yellow',
    4 : 'Orange',
    5 : 'Pink',
    6 : 'Purple',
    7 : 'Brown',
    8 : 'Grey',
    9 : 'Black',
    10 : 'White'
}
app=flask.Flask(__name__)
#app.config["DEBUG"]=True
#predicting from loaded trained_model


@app.route('/')
def home():
    return "<h1>working</h1>"


@app.route('/api/',methods=['POST'])
def classifier():
    return jsonify("resultfromrgb")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
