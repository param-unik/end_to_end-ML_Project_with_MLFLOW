from flask import Flask, render_template, request, redirect
import os
import pandas as pd
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route('/train', methods=['GET'])
def model_training():
    os.system("python main.py")
    return "Training successfully completed!"


@app.route('/predict', methods=['GET', 'POST'])
def model_predict():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            pH = float(request.form['pH'])
            density = float(request.form['density'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                    free_sulfur_dioxide, total_sulfur_dioxide, pH, density, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)

            print(data)

            model = PredictionPipeline()
            prediction = model.predict(data)

            return render_template("results.html", prediction=str(prediction))

        except Exception as e:
            print('An error occurred as : ', e)
            return 'Something went wrong!'
    else:
        return 'Something went wrong! GET request received!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)