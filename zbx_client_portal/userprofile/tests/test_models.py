from unittest.mock import patch
from django.apps import apps
from django.db import IntegrityError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase


@patch('userprofile.models.ZabbixGateway')
class UserProfileModelsTestCase(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.raw_password = 'test_password'
        self.user = get_user_model().objects.create_user(self.username, self.raw_password)
        self.UserProfile = apps.get_model('userprofile', 'UserProfile')
        self.Language = apps.get_model('userprofile', 'Language')

    def test_get_zabbix_info(self, gw):
        pass

    def test_create_zabbix_user(self, gw):
        pass

    def test_default_profile(self, gw):
        profile = self.UserProfile.get_default()
        self.assertIsNotNone(profile.language)
        self.assertIsNone(profile.pk)
        self.assertEqual(profile.language.language_code, settings.LANGUAGE_CODE)
        self.Language.objects.all().delete()
        self.assertEqual(self.Language.objects.count(), 0)

    def test_save_profile(self, gw):
        gw.create_zabbix_user.return_value = 7
        profile = self.UserProfile.get_default()
        profile.user = self.user
        with self.assertRaises(IntegrityError):
            profile.save()
        profile.save(username=self.username, raw_password=self.raw_password)
