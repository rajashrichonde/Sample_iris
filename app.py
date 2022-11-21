from project_app.utils import IrisSpecies
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page"

@app.route('/predict')
def predict():
    input = request.get_json()
    print(input)
    SepalLengthCm = input['SepalLengthCm']
    SepalWidthCm = input['SepalWidthCm']
    PetalLengthCm = input['PetalLengthCm']
    PetalWidthCm = input['PetalWidthCm']

    obj = IrisSpecies(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    output = obj.predict_species()

    return jsonify({"Result":output})



if __name__ == '__main__':
    app.run()