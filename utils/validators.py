import re

from django import forms


def validateCPF(cpf: str):
    """Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    Parâmetros:
        cpf (str): CPF a ser validado

    Erros:
        - Erro, quando o CPF não possuir o formato 999.999.999-99;
        - Erro, quando o CPF não possuir 11 caracteres numéricos;
        - Erro, quando os dígitos verificadores forem inválidos;

    Exemplos:

    >>> validate('529.982.247-25')
    Sem erro
    >>> validate('52998224725')
    Erro
    >>> validate('111.111.111-11')
    Erro
    """

    # Verifica a formatação do CPF
    if not re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
        raise forms.ValidationError(
            "CPF inválido. Formato incorreto de CPF.", code="invalid"
        )

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        raise forms.ValidationError(
            "CPF inválido. Dígitos insuficientes ou dígitos iguais.", code="invalid"
        )

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        raise forms.ValidationError("CPF inválido.", code="invalid")

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        raise forms.ValidationError("CPF inválido.", code="invalid")
