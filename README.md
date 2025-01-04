# Customer Churn Prediction

This project demonstrates a **Customer Churn Prediction System** that predicts whether a customer is likely to churn based on historical data. The machine learning model is built using **XGBoost** and deployed as a RESTful API using **Flask**. The application is live and hosted on **Render**.

---

## **Features**
- **Data Handling**:
  - Dataset: [Kaggle’s Telecom Customer Churn Dataset](https://www.kaggle.com/datasets).
  - Comprehensive preprocessing:
    - Handled missing values.
    - Encoded categorical features.
    - Scaled numerical features.
  - Feature engineering to improve prediction accuracy.

- **Model Training**:
  - Used **XGBoost**, a robust gradient boosting algorithm, for classification.
  - Tuned hyperparameters to optimize model performance.

- **Deployment**:
  - RESTful API for real-time predictions.
  - Hosted on **Render** at: [Customer Churn Prediction Live App](https://model-customer-churn-5.onrender.com).

- **API Integration**:
  - Accepts JSON input via POST requests.
  - Outputs predictions in JSON format.

---

## **Technical Stack**
1. **Languages**:
   - Python
2. **Libraries**:
   - `pandas`, `numpy` for data preprocessing.
   - `scikit-learn` for feature engineering and metrics evaluation.
   - `xgboost` for model training.
   - `flask` for API development.
3. **Deployment**:
   - **Render** for hosting the live app.

---

## **Dataset**
- **Source**: [Kaggle’s Telecom Customer Churn Dataset](https://www.kaggle.com/datasets).
- **Description**:
  - Features include customer demographics, service details, and contract types.
  - Target variable: `Churn` (binary classification).

---

## **API Documentation**

### **Endpoint**
- **URL**: `https://model-customer-churn-5.onrender.com/predict`
- **Method**: POST

### **Input**
- JSON object containing customer details.
- **Example Input**:
  ```json
  {
      "gender": "Female",
      "SeniorCitizen": 0,
      "Partner": "Yes",
      "Dependents": "No",
      "tenure": 12,
      "PhoneService": "Yes",
      "MultipleLines": "No",
      "InternetService": "Fiber optic",
      "OnlineSecurity": "No",
      "OnlineBackup": "Yes",
      "DeviceProtection": "No",
      "TechSupport": "Yes",
      "StreamingTV": "No",
      "StreamingMovies": "Yes",
      "Contract": "Month-to-month",
      "PaperlessBilling": "Yes",
      "PaymentMethod": "Electronic check",
      "MonthlyCharges": 70.35,
      "TotalCharges": 140.70
  }
Output
JSON object containing the prediction result.
Example Output:
json
Copy code
{
    "prediction": "Churn",
    "probability": 0.78
}
Testing
Postman or Similar Platform:
Use Postman to send POST requests to the API endpoint.
Set the request body as raw JSON with the required fields.
Headers: Content-Type: application/json.
Project Directory Structure
graphql
Copy code
Customer_Churn_Prediction/
│
├── app.py                           # Flask API script
├── train_model.py                   # Script for model training
├── preprocess_data.py               # Data preprocessing script
├── requirements.txt                 # Dependencies
├── README.md                        # Project documentation
├── churn_model/                     # Model directory
│   ├── model.pkl                    # Serialized XGBoost model
│   ├── encoder.pkl                  # Encoded label mappings
│
└── sample_requests/                 # Example input JSON files
    ├── request_example.json
    └── response_example.json
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/qaysSE/model_customer_churn.git
cd model_customer_churn
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the Flask API Locally
bash
Copy code
python app.py
The API will be available at http://127.0.0.1:5000/predict.
4. Test the API
Use curl or Postman:

bash
Copy code
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{
         "gender": "Female",
         "SeniorCitizen": 0,
         "Partner": "Yes",
         "Dependents": "No",
         "tenure": 12,
         "PhoneService": "Yes",
         "MultipleLines": "No",
         "InternetService": "Fiber optic",
         "OnlineSecurity": "No",
         "OnlineBackup": "Yes",
         "DeviceProtection": "No",
         "TechSupport": "Yes",
         "StreamingTV": "No",
         "StreamingMovies": "Yes",
         "Contract": "Month-to-month",
         "PaperlessBilling": "Yes",
         "PaymentMethod": "Electronic check",
         "MonthlyCharges": 70.35,
         "TotalCharges": 140.70
     }'
Deliverables
Live App: Deployed on Render.
GitHub Repository: Includes all code and instructions for reproducing the project.
Documentation: Clear README.md with project details, setup instructions, and API documentation.
Future Enhancements
Add a front-end interface for easier interaction with the model.
Implement model retraining using fresh data.
Deploy on AWS for scalability.
Contact
For questions or suggestions, feel free to reach out at qayshajibrahim@gmail.com.




