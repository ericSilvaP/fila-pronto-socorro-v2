from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=65)
    dad = models.CharField(max_length=65, null=True, blank=True)
    mom = models.CharField(max_length=65, null=True, blank=True)
    cpf = models.CharField(max_length=14)
    birth_date = models.DateField()
    sus_card = models.CharField(max_length=15, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField()
    blood_type = models.CharField(max_length=3, null=True, blank=True)
