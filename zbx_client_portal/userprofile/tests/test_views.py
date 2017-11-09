from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user('test_user')

    def test_login(self):
        response = self.client.get(reverse('userprofile:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(reverse('userprofile:logout'))
        self.assertRedirects(response, reverse('userprofile:login'))

    def test_account(self):
        response = self.client.get(reverse('userprofile:account'))
        self.assertRedirects(response, reverse('userprofile:login'))
        self.client.force_login(self.user)
        response = self.client.get(reverse('userprofile:account'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get(reverse('userprofile:register'))
        self.assertRedirects(response, reverse('userprofile:login'))
        self.client.force_login(self.user)
        response = self.client.get(reverse('userprofile:register'))
        self.assertEqual(response.status_code, 200)
