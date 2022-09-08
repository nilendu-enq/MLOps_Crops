
from flask import Flask, send_file, make_response,jsonify, request
import pickle
import pandas as pd
import json

app = Flask(__name__)

model_filename = 'models/model.sav'
scaler_filename = 'models/scaler.sav'
y_label_filename = 'dataset/split/y_label.csv'

loaded_scaler = pickle.load(open(scaler_filename, 'rb')) 
loaded_model = pickle.load(open(model_filename, 'rb'))

y_label=pd.read_csv(y_label_filename).to_dict()['0']

@app.route('/', methods=['GET'])
def home():
    return '{"message" : "Welcome to prediction model"}'


@app.route('/health_check', methods=['GET'])
def health_check():
    return '{"message" : "Api is working"}'


@app.route('/predict', methods=['POST'])
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
    app.run(host="0.0.0.0", port=8080, debug=True)