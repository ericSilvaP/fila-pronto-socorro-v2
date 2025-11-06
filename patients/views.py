from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import PatientForm


def register_patient(request):
    patient_form_data = request.session.get("patient_form_data")
    form = PatientForm(patient_form_data)
    return render(
        request,
        "patients/pages/patients_list.html",
        {"form": form, "form_action": reverse("patients:create")},
    )


@require_POST
def register_patient_post(request):
    POST = request.POST
    request.session["patient_form_data"] = POST
    form = PatientForm(POST)

    if form.is_valid():
        form.save()
        del request.session["patient_form_data"]

    return redirect("patients:register")
