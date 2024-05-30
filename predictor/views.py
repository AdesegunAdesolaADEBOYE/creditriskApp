import joblib
import numpy as np
from django.shortcuts import render
from .forms import LoanPredictionForm

# Load the models
logistic_model = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/logistic_regression_model.pkl')
xgboost_model = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/xgb_regressor_model.pkl')

def index(request):
    if request.method == 'POST':
        form = LoanPredictionForm(request.POST)
        if form.is_valid():
            person_age = form.cleaned_data['person_age']
            person_income = form.cleaned_data['person_income']
            person_home_ownership = form.cleaned_data['person_home_ownership']
            person_emp_length = form.cleaned_data['person_emp_length']
            loan_intent = form.cleaned_data['loan_intent']
            loan_grade = form.cleaned_data['loan_grade']
            loan_amnt = form.cleaned_data['loan_amnt']
            loan_int_rate = form.cleaned_data['loan_int_rate']
            loan_percent_income = form.cleaned_data['loan_percent_income']
            cb_person_default_on_file = form.cleaned_data['cb_person_default_on_file']
            cb_person_cred_hist_length = form.cleaned_data['cb_person_cred_hist_length']

            # Prepare the data for prediction
            data = np.array([[
                person_age, person_income, person_home_ownership, person_emp_length,
                loan_intent, loan_grade, loan_amnt, loan_int_rate, loan_percent_income,
                cb_person_default_on_file, cb_person_cred_hist_length
            ]])

            # Predict with logistic regression model
            default_prediction = logistic_model.predict(data)[0]

            # Predict with XGBoost regression model
            loan_amount_prediction = xgboost_model.predict(data)[0]

            context = {
                'default_prediction': default_prediction,
                'loan_amount_prediction': loan_amount_prediction,
                'input_data': data[0]
            }

            return render(request, 'result.html', context)
    else:
        form = LoanPredictionForm()

    return render(request, 'index.html', {'form': form})







# from django.shortcuts import render
# from .forms import LoanForm
# from django.http import HttpResponse
# import joblib
# import numpy as np
# import pandas as pd


# # Load the models and encoder
# logistic_model = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/logistic_regression_model.pkl')
# xgboost_model = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/xgb_regressor_model.pkl')
# encoder = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/one_hot_encoder.pkl')

# def index(request):
#     if request.method == 'POST':
#         # Get form data
#         person_age = float(request.POST.get('person_age'))
#         person_income = int(request.POST.get('person_income'))
#         person_home_ownership = request.POST.get('person_home_ownership')
#         person_emp_length = float(request.POST.get('person_emp_length'))
#         loan_intent = request.POST.get('loan_intent')
#         loan_grade = request.POST.get('loan_grade')
#         loan_amnt = int(request.POST.get('loan_amnt'))
#         loan_int_rate = float(request.POST.get('loan_int_rate'))
#         loan_percent_income = float(request.POST.get('loan_percent_income'))
#         cb_person_default_on_file = request.POST.get('cb_person_default_on_file')
#         cb_person_cred_hist_length = int(request.POST.get('cb_person_cred_hist_length'))

#         # Create a DataFrame for the input
#         features_df = pd.DataFrame({
#             'person_age': [person_age],
#             'person_income': [person_income],
#             'person_home_ownership': [person_home_ownership],
#             'person_emp_length': [person_emp_length],
#             'loan_intent': [loan_intent],
#             'loan_grade': [loan_grade],
#             'loan_amnt': [loan_amnt],
#             'loan_int_rate': [loan_int_rate],
#             'loan_percent_income': [loan_percent_income],
#             'cb_person_default_on_file': [cb_person_default_on_file],
#             'cb_person_cred_hist_length': [cb_person_cred_hist_length]
#         })

        
#         # Separate categorical and numerical columns
#         categorical_columns = ['person_home_ownership', 'loan_intent', 'loan_grade', 'cb_person_default_on_file']
#         numerical_columns = [col for col in features_df.columns if col not in categorical_columns]

#         # Encode categorical columns
#         features_encoded = encoder.transform(features_df[categorical_columns])

#         # Combine encoded categorical columns with numerical columns
#         features_final = np.hstack((features_df[numerical_columns].values, features_encoded))

#         # Predict loan default
#         default_prediction = logistic_model.predict(features_final)[0]

#         # Predict loan amount
#         loan_amount_prediction = xgboost_model.predict(features_final)[0]

#         return render(request, 'result.html', {
#                 'default_prediction': default_prediction,
#                 'loan_amount_prediction': loan_amount_prediction
#             })
#     else:
#         form = LoanForm()
#     return render(request, 'index.html', {'form': form})  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    




#     # Separate categorical columns and encode them
    #     categorical_columns = ['person_home_ownership', 'loan_intent', 'loan_grade', 'cb_person_default_on_file']
    #     numerical_columns = [col for col in input_df.columns if col not in categorical_columns]

    #     encoded_categorical = encoder.transform(input_df[categorical_columns])
    #     numerical_data = input_df[numerical_columns].values

    #     # Concatenate numerical and encoded categorical data
    #     final_input = np.hstack((numerical_data, encoded_categorical))

    #     # Predict loan default
    #     loan_default_prediction = logistic_model.predict(final_input)[0]

    #     # Predict appropriate loan amount
    #     loan_amount_prediction = xgboost_model.predict(final_input)[0]

    #     # Prepare context for rendering
    #     context = {
    #         'loan_default_prediction': loan_default_prediction,
    #         'loan_amount_prediction': loan_amount_prediction
    #     }
    #     return render(request, 'index.html', context)

    # return render(request, 'index.html')

# import joblib
# from django.shortcuts import render
# from .forms import LoanForm
# import numpy as np
# import pandas as pd
# from django.http import HttpResponse

# # Create your views here.

# # Load the models and encoder
# logistic_model = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/logistic_regression_model.pkl')
# xgboost_model = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/xgb_regressor_model.pkl')
# encoder = joblib.load('C:/Users/PC/Documents/sola/others/Telegram Desktop/one_hot_encoder.pkl')


# def index(request):
#     if request.method == 'POST':
#         form = LoanForm(request.POST)
#         if form.is_valid():
#             # Process form data and make predictions
#             data = form.cleaned_data
#             features = [
#                 data['person_age'], data['person_income'], data['person_home_ownership'],
#                 data['person_emp_length'], data['loan_intent'], data['loan_grade'],
#                 data['loan_amnt'], data['loan_int_rate'], data['loan_percent_income'],
#                 data['cb_person_default_on_file'], data['cb_person_cred_hist_length']
#             ]
#              # Convert to DataFrame for encoding
#             features_df = pd.DataFrame([features], columns=[
#                 'person_age', 'person_income', 'person_home_ownership',
#                 'person_emp_length', 'loan_intent', 'loan_grade',
#                 'loan_amnt', 'loan_int_rate', 'loan_percent_income',
#                 'cb_person_default_on_file', 'cb_person_cred_hist_length'
#             ])

#             # Separate categorical and numerical columns
#             categorical_columns = ['person_home_ownership', 'loan_intent', 'loan_grade', 'cb_person_default_on_file']
#             numerical_columns = [col for col in features_df.columns if col not in categorical_columns]

#             # Encode categorical columns
#             features_encoded = encoder.transform(features_df[categorical_columns])

#             # Combine encoded categorical columns with numerical columns
#             features_final = np.hstack((features_df[numerical_columns].values, features_encoded))

#             # Predict loan default
#             default_prediction = logistic_model.predict(features_final)[0]

#             # Predict loan amount
#             loan_amount_prediction = xgboost_model.predict(features_final)[0]

#             return render(request, 'result.html', {
#                 'default_prediction': default_prediction,
#                 'loan_amount_prediction': loan_amount_prediction
#             })
#     else:
#         form = LoanForm()
#     return render(request, 'index.html', {'form': form})







# def index(request):
#     result = None
#     if request.method == 'POST':
#         form = LoanForm(request.POST)
#         if form.is_valid():
#             # Extract features from form data
#             features = [form.cleaned_data[field] for field in form.fields]
#             features = encoder.transform([features])
            
#             # Predict loan default
#             loan_default = logistic_model.predict(features)[0]
#             loan_default_proba = logistic_model.predict_proba(features)[0][1]
            
#             # Predict appropriate loan amount
#             loan_amnt = xgboost_model.predict(features)[0]
            
#             result = {
#                 'loan_default': 'Default' if loan_default == 1 else 'Non-Default',
#                 'loan_default_proba': loan_default_proba,
#                 'predicted_loan_amnt': loan_amnt
#             }
#     else:
#         form = LoanForm()
    
#     return render(request, 'predictor/index.html', {'form': form, 'result': result})


