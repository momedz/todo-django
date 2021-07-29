from django.contrib import admin

# Register your models here.
from todo import models

admin.site.register(models.Todo)