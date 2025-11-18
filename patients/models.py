from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=65)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    gender = models.CharField()
    sus_card = models.CharField(max_length=14, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    blood_type = models.CharField(max_length=3, null=True, blank=True)
    dad = models.CharField(max_length=65, null=True, blank=True)
    mom = models.CharField(max_length=65, null=True, blank=True)
