
from flask import Flask, send_file, make_response,jsonify, request
import pickle
import pandas as pd
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

model_filename = 'models/model.sav'
scaler_filename = 'models/scaler.sav'
y_label_filename = 'dataset/split/y_label.csv'
score_filename = 'models/score.sav'

loaded_scaler = pickle.load(open(scaler_filename, 'rb')) 
loaded_model = pickle.load(open(model_filename, 'rb'))
loaded_score = pickle.load(open(score_filename, 'rb'))

y_label=pd.read_csv(y_label_filename).to_dict()['0']

@app.route('/', methods=['GET'])
def home():
    return '{"message" : "Welcome to prediction model"}'


@app.route('/api/v1/health_check', methods=['GET'])
def health_check():
    return '{"message" : "Api is working"}'


@app.route('/api/v1/score', methods=['GET'])
def score():
    return json.dumps({"score":loaded_score})

@app.route('/api/v1/predict', methods=['POST'])
def predict():
  
    data = request.json
    X = pd.DataFrame(data)
    X_scaled = loaded_scaler.transform(X)
    pred = loaded_model.predict(X_scaled)
    pred_list=pred.tolist()
    result = []
    for i in pred_list:
        result.append(y_label[i])

    return json.dumps({"crop_prediction":result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)