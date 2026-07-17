# 🚀 Customer Churn Prediction ML Project

An End-to-End Machine Learning project to predict whether a telecom customer is likely to churn or continue using the service.

This project covers the complete Machine Learning lifecycle:

✅ Data Analysis  
✅ Data Cleaning  
✅ Exploratory Data Analysis  
✅ Feature Engineering  
✅ Model Training  
✅ Model Evaluation  
✅ Model Deployment  
✅ Real-Time Prediction using Streamlit  


# 📌 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based companies.

The main objective of this project is to build a Machine Learning model that can predict whether a customer will leave the telecom service based on customer demographics, service usage, contract details, and billing information.

The trained model is deployed using Streamlit to provide real-time churn predictions.


# 🎯 Business Problem

Telecom companies lose customers due to:

- Poor customer experience
- Pricing issues
- Competition
- Service problems

Predicting customer churn helps companies to:

- Identify customers who may leave
- Improve customer retention
- Provide personalized offers
- Reduce revenue loss
- Make better business decisions


# 📊 Dataset Information

## Dataset

IBM Telco Customer Churn Dataset


## Dataset Details

- Total Records: 7043
- Original Features: 21
- Final ML Features: 30


## Features Include

### Customer Information

- Gender
- Senior Citizen
- Partner
- Dependents


### Service Information

- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies


### Account Information

- Tenure
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges


# 🎯 Target Variable

## Churn

Values:

- Yes → Customer will leave the service
- No → Customer will continue service


# 🛠️ Technologies Used

## Programming Language

- Python


## Data Processing

- Pandas
- NumPy


## Data Visualization

- Matplotlib
- Seaborn


## Machine Learning

- Scikit-learn


## Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier


## Deployment

- Streamlit


## Development Tools

- VS Code
- Jupyter Notebook
- Git
- GitHub


# 🏗️ Project Structure


Customer-Churn-Prediction-ML
│
├── data
│ │
│ ├── raw
│ │ └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│ │
│ └── processed
│ ├── X_train.csv
│ ├── X_test.csv
│ ├── y_train.csv
│ └── y_test.csv
│
├── notebooks
│ │
│ ├── 01_EDA.ipynb
│ ├── 02_Feature_Engineering.ipynb
│ └── 03_Model_Training.ipynb
│
├── models
│ └── random_forest_model.pkl
│
├── src
│ │
│ ├── data_preprocessing.py
│ ├── train.py
│ └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE



# 🔄 Machine Learning Workflow


## 1. Data Loading

Loaded telecom customer churn dataset using Pandas.


## 2. Exploratory Data Analysis (EDA)

Performed:

✅ Dataset shape analysis  
✅ Column analysis  
✅ Data type checking  
✅ Missing value detection  
✅ Duplicate checking  
✅ Churn distribution analysis  
✅ Numerical feature analysis  
✅ Categorical feature analysis  
✅ Correlation analysis  
✅ Outlier detection  


## 3. Data Preprocessing

Performed following steps:

- Converted TotalCharges into numerical format
- Removed unnecessary customerID column
- Handled missing values
- Separated features and target variable
- Applied One-Hot Encoding
- Performed train-test split
- Prepared dataset for Machine Learning


## 4. Model Training

Multiple Machine Learning algorithms were trained:

### Logistic Regression

Used as baseline classification model.


### Decision Tree Classifier

Used to capture non-linear patterns.


### Random Forest Classifier

Selected as final model because of better performance and stability.


# 📈 Model Evaluation

Models were evaluated using:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score


Final trained model:models/random_forest_model.pkl



# 🚀 Streamlit Web Application

The trained model is deployed using Streamlit.

## Application Features

✅ User-friendly interface  
✅ Customer details input  
✅ Real-time prediction  
✅ Churn probability analysis  
✅ Instant results  


## Run Application

```bash
🖥️ Application Flow

The application works through the following pipeline:

User Input
    |
    ↓
Data Processing
    |
    ↓
Feature Transformation
    |
    ↓
Random Forest Model
    |
    ↓
Prediction Result

Output:

✅ Customer Will Stay
❌ Customer Will Churn
⚙️ Installation & Setup
Clone Repository
git clone https://github.com/shaikyusufvali/Customer-Churn-Prediction-ML.git
Move Into Project Folder
cd Customer-Churn-Prediction-ML
Create Virtual Environment
python -m venv venv
Activate Environment

Windows:

venv\Scripts\activate
Install Required Libraries
pip install -r requirements.txt
Run Streamlit Application
streamlit run app.py
🔮 Future Improvements

Planned improvements:

🚀 Hyperparameter tuning using GridSearchCV
🚀 XGBoost and LightGBM model implementation
🚀 SHAP based model explainability
🚀 Cloud deployment using AWS/Azure
🚀 Automated Machine Learning pipeline
🚀 Customer retention recommendation system
🚀 CI/CD integration
👨‍💻 Author
Shaik Yusuf Vali

Artificial Intelligence & Machine Learning Student

Skills

Python | SQL | Machine Learning | Data Analysis | Artificial Intelligence | Generative AI

⭐ Project Highlights

✅ Complete End-to-End Machine Learning Project
✅ Industry Standard Project Structure
✅ Data Cleaning & Feature Engineering Pipeline
✅ Multiple ML Algorithms Tested
✅ Random Forest Model Deployment
✅ Real-Time Prediction using Streamlit
✅ GitHub Portfolio Ready

📌 Conclusion

This project demonstrates how Machine Learning can be applied to solve real-world business problems by predicting customer churn.

The system helps companies identify potential churn customers, improve retention strategies, and make better data-driven decisions.

⭐ If you like this project, consider giving it a star!

