Model Customer Churn
This project predicts customer churn in a telecommunications company. It uses a trained machine learning model (saved as churn_model.pkl) built with scikit-learn and Flask to expose predictions through an API. The project is deployed on Render.

Key Features
Trained Model: A churn prediction model trained using scikit-learn, stored as churn_model.pkl.
Data Preprocessing: Handles binary, multi-category encoding, and missing values using LabelEncoder and one-hot encoding.
API for Predictions: Exposes a /predict endpoint to get churn predictions.
Model Deployment: Deployed as a web service on Render, allowing real-time predictions.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/qaysSE/model_customer_churn.git
cd model_customer_churn
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Running Locally:
To start the Flask server:

bash
Copy code
python customer_churn.py
API Endpoint:
POST /predict: This endpoint accepts customer data in JSON format and returns the churn prediction. Example request:

json
Copy code
{
  "gender": "Female",
  "Partner": "Yes",
  "Dependents": "No",
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "Yes",
  "DeviceProtection": "Yes",
  "TechSupport": "Yes",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "One year",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check"
}
Example response:

json
Copy code
{
  "churn": 1
}
Trained Model
The model is trained to predict customer churn using customer features like gender, payment methods, services used, etc.
The model was trained using scikit-learn, and the trained model is stored in the file bin/churn_model.pkl.
Model input preprocessing (encoding and handling missing values) is done in the function preprocess_data().
Deployment
Deployed on Render at: https://model-customer-churn-5.onrender.com/

Deployment Steps:
Push changes to GitHub.
Create a web service on Render, setting up the following Procfile:
makefile
Copy code
web: gunicorn customer_churn:app
Include a requirements.txt file with all dependencies.
Technologies Used
Python
Flask for API
scikit-learn for model training and prediction
Render for deployment
pandas for data processing
joblib for saving/loading the trained model
Contributing
Feel free to fork, open issues, or submit pull requests. Contributions are welcome!
