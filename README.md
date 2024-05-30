This is a Capstone Project by the following members of Group 7, Data Science Track of INGRYD ACADEMY;

Christiana Abolarin
Aisha Imonikhe
Emmanuel Nehemiah
Muideen Oyediran
Adesegun Adeboye

The dataset used has 12 columns and 32,581 rows, sourced from Malaysia.

Project Title — Credit Risk Assessment for Loan Approvals
Objectives —- Assess the creditworthiness of loan applicants and minimize default risks.

We used 2 Machine Learning models - Logistic Regression for Classification, to predict whether an applicant will default or not.
And XGBoost Regression, XRegressor, to generate an appropriate Loan Amount irrespective of the amount applied for by the borrower.

The dataset was cleaned to replace NaN values in 3 columns, unrealistic fields were replaced with median values of the 'person_emp_length' and 'loan_int_rate' columns.
There are 4 categorical columns, 'person_home_ownership', 'loan_intent', 'loan_grade', and 'cb_person_default_on_file', which were all manually transformed into numerical ones 
to avoid using an encoder. We tried using the One-Hot-Encoder but hit a brick wall at the deployment point when the features expected and received
differed.

Exploratory Data Analysis was done using Univariate and Multivariate Analysis to gain Data-driven insights - Histogram, Scatterplot, HeatMap, etc.

Logistic Regression and XGBoost Regression were imported, and the features were prepared, and further split into Training and Test sets. We performed Standardization using StandardScaler
on the X-train and X_test. The model was instantiated, after which Model Prediction and Evaluation were done. 

Logistic Regression model performance was 0.84 and an F1 score of 0.90/0.56
Also, for the Logistic Regression;
Mean Squared Error, MSE =>> 0.16
Mean Absolute Error, MAE =>> 0.16
R-Square =>> 0.08

XGBoost Regression model performance are;
Mean Squared Error, MSE =>> 168146
The Root Mean Squared Error, RMSE =>> 410

The trained models were dumped using joblib, and loaded in the Django App - loan_app (Django-admin startproject loan_app). The simple app used Django, HTML, and Bootstrap.

