from django.test.testcases import SimpleTestCase
from django.urls import reverse, resolve
from patients import views


class PatientsViewsTest(SimpleTestCase):
    def test_patients_register_view_is_ok(self):
        view = resolve(reverse("patients:register"))
        self.assertIs(view.func, views.register_patient)

    def test_patients_register_post_view_is_ok(self):
        view = resolve(reverse("patients:create"))
        self.assertIs(view.func, views.register_patient_post)

    def test_patients_register_post_view_raises_405_on_GET(self):
        url = reverse("patients:create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_patients_register_post_view_redirects_to_register(self):
        url = reverse("patients:create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        response = self.client.post(url, follow=True)
        self.assertTemplateUsed(response, "patients/pages/patients_list.html")
