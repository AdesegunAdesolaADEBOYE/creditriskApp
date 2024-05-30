from django import forms

class CaseInsensitiveChoiceField(forms.ChoiceField):
    def clean(self, value):
        value = super().clean(value)
        if isinstance(value, str):
            value = value.lower()
        for choice_value, _ in self.choices:
            if str(choice_value).lower() == value:
                return choice_value
        raise forms.ValidationError(f'Invalid choice: {value}')

class LoanPredictionForm(forms.Form):
    person_age = forms.FloatField(label='Age')
    person_income = forms.IntegerField(label='Income')
    person_home_ownership = CaseInsensitiveChoiceField(
        label='Home Ownership',
        choices=[(0, 'RENT'), (1, 'OWN'), (2, 'MORTGAGE'), (3, 'OTHER')]
    )
    person_emp_length = forms.FloatField(label='Employment Length (years)')
    loan_intent = CaseInsensitiveChoiceField(
        label='Loan Intent',
        choices=[
            (0, 'EDUCATION'), (1, 'PERSONAL'), (2, 'MEDICAL'),
            (3, 'VENTURE'), (4, 'HOMEIMPROVEMENT'), (5, 'DEBTCONSOLIDATION')
        ]
    )
    loan_grade = CaseInsensitiveChoiceField(
        label='Loan Grade',
        choices=[
            (0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'),
            (4, 'E'), (5, 'F'), (6, 'G')
        ]
    )
    loan_amnt = forms.IntegerField(label='Loan Amount')
    loan_int_rate = forms.FloatField(label='Interest Rate (%)')
    loan_percent_income = forms.FloatField(label='Loan Percent Income')
    cb_person_default_on_file = CaseInsensitiveChoiceField(
        label='Credit Bureau Default on File',
        choices=[(0, 'No'), (1, 'Yes')]
    )
    cb_person_cred_hist_length = forms.IntegerField(label='Credit History Length')







# from django import forms

# class LoanForm(forms.Form):
#     person_age = forms.FloatField()
#     person_income = forms.IntegerField()
#     person_home_ownership = forms.CharField()
#     person_emp_length = forms.FloatField()
#     loan_intent = forms.CharField()
#     loan_grade = forms.CharField()
#     loan_amnt = forms.IntegerField()
#     loan_int_rate = forms.FloatField()
#     loan_percent_income = forms.FloatField()
#     cb_person_default_on_file = forms.CharField()
#     cb_person_cred_hist_length = forms.IntegerField()

