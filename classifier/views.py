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
        chestPainScore = form.cleaned_data['chestPainScore']
        restingBP = form.cleaned_data['restingBP']
        cholesterol = form.cleaned_data['cholesterol']
        fastingGlucose = 1 if form.cleaned_data['fastingGlucose'] == 'yes' else 0
        maxHeartRate = form.cleaned_data['maxHeartRate']
        exerciseAngina = 1 if form.cleaned_data['exerciseAngina'] == 'yes' else 0

    result = getPredictions(age, sex, chestPainScore, restingBP, cholesterol,
                            fastingGlucose, maxHeartRate, exerciseAngina)

    return render(request, 'classifier/result.html', {'result': result})


def techniques(request):
    return render(request, 'classifier/techniques.html')


def getPredictions(age, sex, chestPainScore, restingBP, cholesterol, fastingGlucose, maxHeartRate, exerciseAngina):
    import pickle
    modelFolder = settings.BASE_DIR + '/model/'
    model = pickle.load(
        open(os.path.join(modelFolder, os.path.basename("model.pkl")), "rb"))
    scaler = pickle.load(
        open(os.path.join(modelFolder, os.path.basename("scaler.pkl")), "rb"))
    prediction = model.predict(scaler.transform(
        [[age, sex, chestPainScore, restingBP, cholesterol, fastingGlucose, maxHeartRate, exerciseAngina]]))

    if prediction == 0:
        return "No Cardiac Disease"
    elif prediction == 1:
        return "Cardiac Disease"
    else:
        return "Error"
