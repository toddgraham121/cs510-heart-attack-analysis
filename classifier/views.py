from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .models import Technique
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
    ml_techniques = Technique.objects.order_by('-accuracy')
    return render(request, 'classifier/techniques.html', {'ml_techniques': ml_techniques})


def techniquesDetails(request, technique_id):
    techniqueDetail = get_object_or_404(Technique, pk=technique_id)
    return render(request, 'classifier/techniqueDetail.html', {'techniqueDetail': techniqueDetail})


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
        return "Our model predicts that you do NOT have Cardiovascular Disease"
    elif prediction == 1:
        return "Our model predicts you may have Cardiovascular Disease"
    else:
        return "Error"
