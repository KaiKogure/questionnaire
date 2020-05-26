from django.db import models
from titles.models import Title
# Create your models here.


class Question(models.Model):
    name  = models.CharField(max_length=100, blank=True, null=True)
    title = models.ForeignKey(Title, on_delete=models.PROTECT)
    a =  models.CharField(max_length=300, blank=True, null=True)
    b =  models.CharField(max_length=300, blank=True, null=True)
    c =  models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title.name

