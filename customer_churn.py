from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("/Users/qayshajibrahem/model01/bin/churn_model.pkl")

# Preprocessing function to match model training
def preprocess_data(data):
    # List of binary and multi-category columns
    binary_columns = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    multi_category_columns = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
                              'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
                              'Contract', 'PaymentMethod']
    
    # Label encode binary columns
    label_encoders = {}  # Store label encoders for each binary column
    for col in binary_columns:
        if col in data.columns:
            le = LabelEncoder()
            le.fit(data[col].astype(str))  # Fit encoder on the data
            data[col] = le.transform(data[col].astype(str))
            label_encoders[col] = le

    # One-hot encode multi-category columns
    data_encoded = pd.get_dummies(data, columns=multi_category_columns)

    # Ensure any missing values are handled (replace NaN with 0)
    data_encoded = data_encoded.fillna(0)

    # Align the input columns with the model's expected feature names
    missing_cols = set(model.feature_names_in_) - set(data_encoded.columns)
    for col in missing_cols:
        data_encoded[col] = 0

    # Ensure the columns are in the same order as the model's expected input
    data_encoded = data_encoded[model.feature_names_in_]

    return data_encoded

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    # Preprocess the data (apply one-hot encoding or label encoding)
    df = preprocess_data(df)

    # Make prediction
    prediction = model.predict(df)

    # Return the prediction in a JSON response
    return jsonify({"churn": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
