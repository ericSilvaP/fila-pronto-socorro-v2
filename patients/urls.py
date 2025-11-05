from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path("cadastro/", views.register_patient, name="register"),
    path("criar/", views.register_patient_post, name="create"),
]
