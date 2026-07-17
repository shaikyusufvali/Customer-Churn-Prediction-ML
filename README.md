# 🚀 Customer Churn Prediction ML Project

An End-to-End Machine Learning Project to predict whether a telecom customer is likely to churn or continue using the service.

This project covers the complete Machine Learning lifecycle:

- Data Analysis
- Data Cleaning
- Feature Engineering
- Model Training
- Model Evaluation
- Model Deployment
- Real-Time Prediction using Streamlit

---

# 📌 Project Overview

Customer churn is a major challenge for subscription-based companies.

The objective of this project is to build a Machine Learning model that predicts whether a customer will leave the telecom service based on customer demographics, services, contract details, and billing information.

The trained model is deployed as a Streamlit web application where users can enter customer details and receive instant churn predictions.

---

# 🎯 Business Problem

Telecom companies lose customers every year due to service issues, pricing, competition, and customer experience.

Predicting churn helps businesses:

- Identify customers who are likely to leave
- Improve customer retention strategies
- Provide personalized offers
- Reduce revenue loss
- Make data-driven decisions

---

# 📊 Dataset Information

## Dataset

**IBM Telco Customer Churn Dataset**

## Dataset Size

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
- Streaming Services

### Account Information

- Tenure
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges

---

# 🎯 Target Variable

Target column:


Churn


Values:


Yes → Customer Churn
No → Customer Stayed


---

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

Algorithms:

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

---


---

### 3) Project Structure 


```markdown
```text
Customer-Churn-Prediction-ML
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   └── 03_Model_Training.ipynb
│
├── models
│   └── random_forest_model.pkl
│
├── src
│   ├── data_preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
└── README.md


---

# 🔄 Machine Learning Workflow

## 1. Data Loading

Loaded telecom customer churn dataset using Pandas.

---

# 2. Exploratory Data Analysis (EDA)

Performed detailed analysis:

✔ Dataset shape checking  
✔ Column analysis  
✔ Data type analysis  
✔ Missing value detection  
✔ Duplicate checking  
✔ Churn distribution analysis  
✔ Numerical feature visualization  
✔ Categorical feature analysis  
✔ Correlation analysis  
✔ Outlier detection  

---

# 3. Data Preprocessing

Steps performed:

- Converted TotalCharges into numerical datatype
- Removed unnecessary customer ID column
- Handled missing values
- Separated features and target variable
- Applied One-Hot Encoding
- Performed train-test split
- Prepared data for Machine Learning models

Final dataset:


Training Features: 30


---

# 4. Model Training

Multiple Machine Learning algorithms were trained:

## Logistic Regression

Used as baseline classification model.

## Decision Tree Classifier

Used to capture non-linear relationships.

## Random Forest Classifier

Used as final model because of better performance and stability.

---

# 📈 Model Evaluation

Models were evaluated using:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score

Random Forest Classifier was selected as the final deployment model.

Saved model:


models/random_forest_model.pkl


---

# 🚀 Streamlit Web Application

The trained Machine Learning model is deployed using Streamlit.

## Application Features

✔ User-friendly interface  
✔ Customer information input  
✔ Real-time prediction  
✔ Churn probability decision  
✔ Instant results  


Run application:

```bash
streamlit run app.py

🖥️ Application Flow
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

Churn / Not Churn
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
Install Dependencies
pip install -r requirements.txt
Run Application
streamlit run app.py
📦 Requirements

Main libraries:

pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
🔮 Future Improvements

Planned improvements:

Hyperparameter tuning using GridSearchCV
XGBoost and LightGBM implementation
SHAP based model explainability
Cloud deployment using AWS/Azure
Automated ML pipeline
Customer retention recommendation system
CI/CD integration
👨‍💻 Author
Shaik Yusuf Vali

Artificial Intelligence & Machine Learning Student

Interested Areas:

Machine Learning
Artificial Intelligence
Generative AI
Data Science

Skills:

Python | SQL | Machine Learning | Data Analysis | AI
⭐ Project Highlights

✅ Complete End-to-End Machine Learning Project
✅ Industry-style Folder Structure
✅ Data Preprocessing Pipeline
✅ Multiple ML Models Tested
✅ Model Deployment Using Streamlit
✅ Real-Time Prediction System
✅ GitHub Portfolio Ready

📌 Conclusion

This project demonstrates how Machine Learning can be used to solve real-world business problems by predicting customer churn and helping companies improve customer retention.

⭐ If you like this project, consider giving it a star!