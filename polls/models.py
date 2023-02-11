import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.TextField(max_length=200)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        date_today = timezone.now()
        date_yesterday = date_today - datetime.timedelta(days=1) 
        return date_yesterday <= self.date_created <= date_today


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100) 
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

