
from flask import Flask, send_file, make_response,jsonify, request
import pickle
import pandas as pd
import json

app = Flask(__name__)

model_filename = 'models/knn.sav'
scaler_filename = 'models/scaler.sav'

loaded_scaler = pickle.load(open(scaler_filename, 'rb')) 
loaded_model = pickle.load(open(model_filename, 'rb'))

@app.route('/', methods=['GET'])
def home():
    return '{"message" : "Welcome to prediction model"}'


@app.route('/health_check', methods=['GET'])
def health_check():
    return '{"message" : "Api is working"}'


@app.route('/predict', methods=['POST'])
def predict():
  
    data = request.json
    print(request.json)
    X = pd.DataFrame(data)
    print(X)
    X_scaled = loaded_scaler.transform(X)
    result = loaded_model.predict(X_scaled)
    
    return json.dumps(result.tolist())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)