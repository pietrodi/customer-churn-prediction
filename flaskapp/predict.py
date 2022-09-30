import pickle
from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd

from scripts.prepare_data import prepare_data

app = Flask('bank-churn')

model_file = 'model.pkl'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/predict', methods = ['POST'])
def predict():
    customer = request.get_json()
    customer_df = pd.json_normalize(customer)
    predict_df = prepare_data(customer_df)

    y_pred = model.predict_proba(predict_df)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 9696)