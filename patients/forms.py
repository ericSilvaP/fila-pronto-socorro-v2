from django import forms
from patients.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

    name = forms.CharField(
        label="Nome",
        error_messages={"required": "Preencha este campo"},
    )
    cpf = forms.CharField(
        label="CPF",
        error_messages={"required": "Preencha este campo"},
    )
    birth_date = forms.DateField(
        label="Data de Nascimento",
        error_messages={"required": "Preencha este campo"},
    )
    sus_card = forms.CharField(
        label="Número do SUS",
        max_length=14,
        error_messages={"required": "Preencha este campo"},
    )
    dad = forms.CharField(
        label="Nome do Pai",
        required=False,
    )
    mom = forms.CharField(
        label="Nome da Mãe",
        required=False,
    )
    phone_number = forms.CharField(label="Telefone", required=False)

    gender = forms.ChoiceField(
        label="Gênero",
        choices=(
            ("f", "Feminino"),
            ("m", "Masculino"),
            ("i", "Indefinido"),
        ),
    )
    blood_type = forms.ChoiceField(
        label="Tipo Sanguíneo",
        required=False,
        choices=(
            ("i", "Não Sei"),
            ("a+", "A+"),
            ("a-", "A-"),
            ("b+", "B+"),
            ("b-", "B-"),
            ("ab-", "AB-"),
            ("ab+", "AB+"),
            ("o+", "O+"),
            ("o-", "O-"),
        ),
    )
