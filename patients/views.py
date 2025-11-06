from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import PatientForm


# Create your views here.
def register_patient(request):
    form = PatientForm()
    return render(request, "patients/pages/patients_list.html", {"form": form})


@require_POST
def register_patient_post(request):
    form = PatientForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect("patients:register")
