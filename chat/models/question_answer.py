from django.db import models
from django.contrib.postgres.fields import ArrayField


class QuestionAnswer(models.Model):
    answers = ArrayField(models.CharField(max_length=512))
    qText = models.TextField(blank=True)
