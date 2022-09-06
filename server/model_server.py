
from flask import Flask, send_file, make_response,jsonify, request
import pickle
import pandas as pd
import json
import boto3

ACCESS_KEY = 'AKIAWATRK4TZJTQ4BA2I'
SECRET_KEY = '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'

app = Flask(__name__)

model_filename = 'knn.sav'
scaler_filename = 'scaler.sav'
y_label_filename = 'y_label.csv'

@app.route('/', methods=['GET'])
def home():
    return '{"message" : "Welcome to prediction model"}'


@app.route('/health_check', methods=['GET'])
def health_check():
    return '{"message" : "Api is working"}'


@app.route('/predict', methods=['POST'])
def predict():

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY , aws_secret_access_key=SECRET_KEY)
    s3.download_file('enq-dataops-pipeline-artifacts', model_filename, f'server/{model_filename}')
    s3.download_file('enq-dataops-pipeline-artifacts', scaler_filename, f'server/{scaler_filename}')
    s3.download_file('enq-dataops-pipeline-artifacts', y_label_filename, f'server/{y_label_filename}')
    
    loaded_model = pickle.load(open(f'server/{model_filename}', 'rb'))
    loaded_scaler = pickle.load(open(f'server/{scaler_filename}', 'rb')) 

    y_label=pd.read_csv(f'server/{y_label_filename}').to_dict()['0']

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