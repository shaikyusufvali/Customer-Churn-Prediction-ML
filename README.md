🚀 Customer Churn Prediction ML Project

An End-to-End Machine Learning project to predict whether a telecom customer is likely to churn or continue using the service.

This project includes complete Machine Learning workflow:

Data Analysis
Data Cleaning
Feature Engineering
Model Training
Model Evaluation
Model Deployment
Real-Time Prediction using Streamlit
📌 Project Overview

Customer churn is a major challenge for telecom companies. The objective of this project is to build a Machine Learning model that predicts customer churn based on customer demographics, services, contract details, and billing information.

The trained model is deployed using Streamlit to provide real-time churn predictions.

🎯 Business Objective

This project helps businesses to:

Identify customers who are likely to leave
Improve customer retention strategies
Reduce revenue loss
Make data-driven decisions
📊 Dataset Information

Dataset: IBM Telco Customer Churn Dataset

Total Records: 7043
Original Features: 21
Final ML Features: 30

Features include:

Customer details
Service information
Contract details
Payment details
Billing information

Target Variable:

Churn

Yes → Customer will churn
No → Customer will stay
🛠️ Technologies Used

Programming Language:

Python

Libraries:

Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib

Machine Learning Models:

Logistic Regression
Decision Tree Classifier
Random Forest Classifier

Deployment:

Streamlit

Tools:

VS Code
Jupyter Notebook
Git
GitHub
🏗️ Project Structure

Customer-Churn-Prediction-ML

data
raw
processed
notebooks
01_EDA.ipynb
02_Feature_Engineering.ipynb
03_Model_Training.ipynb
models
random_forest_model.pkl
src
data_preprocessing.py
train.py
predict.py
app.py
requirements.txt
README.md
🔄 Machine Learning Workflow
Exploratory Data Analysis (EDA)

Performed:

Dataset analysis
Data type checking
Missing value detection
Duplicate checking
Churn distribution analysis
Numerical feature analysis
Categorical feature analysis
Correlation analysis
Data Preprocessing

Steps performed:

Converted TotalCharges into numerical format
Removed unnecessary customer ID column
Handled missing values
Applied One-Hot Encoding
Performed train-test split
Prepared ML-ready dataset
Model Training

Trained multiple classification models:

Logistic Regression
Decision Tree Classifier
Random Forest Classifier

Random Forest was selected as the final model because of better performance and stability.

📈 Model Evaluation

Models were evaluated using:

Accuracy Score
Precision Score
Recall Score
F1 Score

Final saved model:

models/random_forest_model.pkl

🚀 Streamlit Application

The trained Machine Learning model is deployed using Streamlit.

Application Features:

User-friendly interface
Customer information input
Real-time churn prediction
Instant prediction result

Run Application:

streamlit run app.py

⚙️ Installation & Setup

Clone Repository:

git clone https://github.com/shaikyusufvali/Customer-Churn-Prediction-ML.git

Install Dependencies:

pip install -r requirements.txt

Run Application:

streamlit run app.py

🔮 Future Improvements
Hyperparameter tuning using GridSearchCV
XGBoost and LightGBM implementation
SHAP model explainability
Cloud deployment
Automated ML pipeline
Customer retention recommendation system
👨‍💻 Author

Shaik Yusuf Vali

Artificial Intelligence & Machine Learning Student

Skills:

Python | SQL | Machine Learning | Data Analysis | AI

⭐ Project Highlights

✅ End-to-End Machine Learning Project
✅ Industry-style Project Structure
✅ Data Preprocessing Pipeline
✅ Multiple ML Models Tested
✅ Random Forest Deployment
✅ Streamlit Web Application
✅ GitHub Portfolio Ready

📌 Conclusion

This project demonstrates how Machine Learning can solve real-world business problems by predicting customer churn and helping companies improve customer retention using data-driven insights.

⭐ If you like this project, consider giving it a star!
