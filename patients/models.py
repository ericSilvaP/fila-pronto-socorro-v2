from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=65)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    gender = models.CharField()
    sus_card = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=11, null=True)
    blood_type = models.CharField(max_length=3, null=True)
    dad = models.CharField(max_length=65, null=True)
    mom = models.CharField(max_length=65, null=True)
