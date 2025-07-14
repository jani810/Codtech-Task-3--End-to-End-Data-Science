
from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model_file = "iris_model.pkl"
scaler, model = pickle.load(open(model_file, "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = scaler.transform([features])
        prediction = model.predict(final_features)
        classes = ["Setosa", "Versicolor", "Virginica"]
        result = classes[prediction[0]]
        return render_template("index.html", prediction_text=f'Iris Species: {result}')
    except:
        return render_template("index.html", prediction_text='Error: Invalid Input')

if __name__ == "__main__":
    app.run(debug=True)
