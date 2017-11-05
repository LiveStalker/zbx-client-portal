from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse
from django.conf import settings


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get(reverse('userprofile:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(reverse('userprofile:logout'))
        self.assertRedirects(response, reverse('portal:index'))
