from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)


TodoRepository = Todo.objects
