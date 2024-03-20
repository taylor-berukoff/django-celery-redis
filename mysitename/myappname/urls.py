from django.urls import path
from . import views

app_name = "myappname"

urlpatterns = [
    path("", views.index, name="index"),
]
