from time import time
from django.db import models
# create Todo Model
class Todo(models.Model):
    title=models.CharField(max_length=25)
    desc=models.TextField()
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
