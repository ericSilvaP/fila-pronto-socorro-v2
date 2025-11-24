from django import forms
from patients.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

    name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={"placeholder": "Ex: João da Silva"}),
        min_length=4,
    )
    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(
            attrs={"placeholder": "Ex: 111111111-11", "class": "form-cpf-field"}
        ),
        max_length=14,
    )
    birth_date = forms.DateField(
        label="Data de Nascimento",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex: DD/MM/AAAA",
                "class": "form-birth-date-field form-date-field",
            }
        ),
    )
    sus_card = forms.CharField(
        label="Número do SUS",
        widget=forms.TextInput(
            attrs={"placeholder": "Ex: 1234567891012345", "class": "form-sus-field"}
        ),
        max_length=15,
    )
    dad = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ex: José da Silva"}),
        label="Nome do Pai",
        required=False,
    )
    mom = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ex: Maria da Silva"}),
        label="Nome da Mãe",
        required=False,
    )
    phone_number = forms.CharField(
        label="Telefone",
        widget=forms.TextInput(
            attrs={"placeholder": "Ex: (99) 9 9999-9999", "class": "form-phone-field"}
        ),
        max_length=14,
        required=False,
    )

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
