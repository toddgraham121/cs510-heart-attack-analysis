from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import sklearn
import os
from .forms import PredictionForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            results(request)
    else:
        form = PredictionForm()

    return render(request, 'classifier/classifierForm.html', {'form': form})


# our result page view
def results(request):
    form = PredictionForm(request.POST)
    if form.is_valid():
        age = form.cleaned_data['age']
        sex = 1 if form.cleaned_data['sex'] == 'male' else 0
        cp = form.cleaned_data['cp']
        trestbps = form.cleaned_data['trestbps']
        chol = form.cleaned_data['chol']
        fbs = form.cleaned_data['fbs']
        restecg = form.cleaned_data['restecg']
        thalach = form.cleaned_data['thalach']
        exang = form.cleaned_data['exang']
        oldpeak = form.cleaned_data['oldpeak']
        slope = form.cleaned_data['slope']
        ca = form.cleaned_data['ca']
        thal = form.cleaned_data['thal']

    result = getPredictions(age, sex, cp, trestbps, chol,
                            fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    return render(request, 'classifier/result.html', {'result': result})


def getPredictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    import pickle
    modelFolder = settings.BASE_DIR + '/model/'
    model = pickle.load(
        open(os.path.join(modelFolder, os.path.basename("model.pkl")), "rb"))
    scaler = pickle.load(
        open(os.path.join(modelFolder, os.path.basename("scaler.pkl")), "rb"))
    prediction = model.predict(scaler.transform(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]))

    if prediction == 0:
        return "No Cardiac Disease"
    elif prediction == 1:
        return "Cardiac Disease"
    else:
        return "Error"
