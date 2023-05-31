from django.db import models

# Create your models here.

class Question(models.Model):
    text_english = models.CharField(max_length=255)


class Choice(models.Model):
    text_english = models.CharField(max_length=255)
    text_turkish = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


class UserAnswer(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
