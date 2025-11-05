from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path("cadastro/", views.register_patient, name="register"),
]
