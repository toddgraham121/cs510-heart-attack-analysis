from django.db import models

# Create your models here.


class Technique(models.Model):
    technique_type = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    accuracy = models.IntegerField(default=0)
    precision = models.IntegerField(default=0)
    recall = models.IntegerField(default=0)
    url = models.CharField(max_length=500)
    confusionMatrix = models.ImageField()
    descImage = models.ImageField()

    def __str__(self):
        return self.technique_type
