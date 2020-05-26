from django.db import models
from django.contrib.auth.models import User
from questions.models import Question
# Create your models here.


class Answer(models.Model):
    selected = models.CharField(max_length=10)
    user     = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.OneToOneField(Question, on_delete=models.PROTECT)

    def __str__(self):
        if self.question.name != None:
            return self.question.name
        else:
            return self.question.id