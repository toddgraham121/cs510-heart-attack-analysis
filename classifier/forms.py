from django import forms


class PredictionForm(forms.Form):
    age = forms.IntegerField(min_value=0, max_value=120, label='Age:')
    sex = forms.CharField(
        label='Sex:', widget=forms.Select(choices=[('male', 'Male'), ('female', 'Female')]))
    cp = forms.IntegerField(min_value=0, max_value=120, label='CP:')
    trestbps = forms.IntegerField(
        min_value=0, max_value=200, label='trestbps:')
    chol = forms.IntegerField(min_value=0, max_value=120, label='chol:')
    fbs = forms.IntegerField(min_value=0, max_value=120, label='fbs:')
    restecg = forms.IntegerField(min_value=0, max_value=120, label='restecg:')
    thalach = forms.IntegerField(min_value=0, max_value=120, label='thalach:')
    exang = forms.IntegerField(min_value=0, max_value=120, label='exang:')
    oldpeak = forms.IntegerField(min_value=0, max_value=120, label='oldpeak:')
    slope = forms.IntegerField(min_value=0, max_value=120, label='slope:')
    ca = forms.IntegerField(min_value=0, max_value=120, label='ca:')
    thal = forms.IntegerField(min_value=0, max_value=120, label='thal:')
