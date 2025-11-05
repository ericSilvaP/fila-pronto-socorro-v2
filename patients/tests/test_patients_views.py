from django.test.testcases import SimpleTestCase
from django.urls import reverse, resolve
from patients import views


class PatientsViewsTest(SimpleTestCase):
    def test_patients_register_view_is_ok(self):
        view = resolve(reverse("patients:register"))
        self.assertIs(view.func, views.register_patient)
