from django.urls import path

from todo import controllers

urlpatterns = [
    path('', controllers.all),
    path('<int:id>/', controllers.by_id),
]
