from django.db import models

# Create your models here.

class toDoList(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
