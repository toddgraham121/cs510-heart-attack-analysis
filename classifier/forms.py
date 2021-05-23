from django import forms


class PredictionForm(forms.Form):
    age = forms.IntegerField(min_value=0, max_value=120, label='Age:')
    sex = forms.CharField(
        label='Sex:', widget=forms.Select(choices=[('male', 'Male'), ('female', 'Female')]))
    chestPainScore = forms.CharField(
        label='Chest Pain:', widget=forms.Select(choices=[(0, 'None'), (1, 'Mild'), (2, 'Moderate'), (3, 'Severe')]))
    restingBP = forms.IntegerField(
        min_value=0, max_value=200, label='Resting systolic blood pressure:')
    cholesterol = forms.IntegerField(
        min_value=0, max_value=600, label='Cholesterol (mg/dl):')
    fastingGlucose = forms.CharField(
        label='Fasting blood sugar > 120mg/dl:', widget=forms.Select(choices=[('yes', 'Yes'), ('no', 'No')]))
    maxHeartRate = forms.IntegerField(
        min_value=0, max_value=250, label='Maximum heart rate (bpm):')
    exerciseAngina = forms.CharField(label='Exercise induced angina:',
                                     widget=forms.Select(choices=[('yes', 'Yes'), ('no', 'No')]))
