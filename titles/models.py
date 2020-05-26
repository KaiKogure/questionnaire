from django.db import models

# Create your models here.


class Title(models.Model):

    name = models.CharField(max_length=200)
    ask  = models.BooleanField(default=True)

    def __str__(self):
        return self.name