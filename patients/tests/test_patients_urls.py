from django.test.testcases import SimpleTestCase
from django.urls import reverse


class PatientsUrlTest(SimpleTestCase):
    def test_patients_register_url_is_ok(self):
        url = reverse("patients:register")
        self.assertEqual(url, "/pacientes/cadastro/")

    def test_patients_register_post_url_is_ok(self):
        url = reverse("patients:create")
        self.assertEqual(url, "/pacientes/criar/")
