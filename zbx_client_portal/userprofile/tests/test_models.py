from unittest.mock import patch
from django.apps import apps
from django.db import IntegrityError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase


@patch('userprofile.models.UserProfile.zabbix_gw')
class UserProfileModelsTestCase(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.raw_password = 'test_password'
        self.user = get_user_model().objects.create_user(self.username, self.raw_password)
        self.UserProfile = apps.get_model('userprofile', 'UserProfile')
        self.UserLanguage = apps.get_model('userprofile', 'UserLanguage')

    def test_get_zabbix_version(self, gw):
        ver = '3.4'
        gw.get_version.return_value = ver
        self.assertEqual(self.UserProfile.get_zabbix_version(), ver)

    def test_get_zabbix_user(self, gw):
        zabbix_user_id = 7
        zabbix_user_alias = 'test_user'
        gw.create_user.return_value = zabbix_user_id
        gw.get_user.return_value = zabbix_user_alias
        profile = self.UserProfile.get_default()
        profile.user = self.user
        profile.zabbix_user_id = zabbix_user_id
        profile.save(username=self.username, raw_password=self.raw_password)
        self.assertEqual(profile.get_zabbix_user(), zabbix_user_alias)

    def test_create_zabbix_user(self, gw):
        zabbix_user_id = 7
        gw.create_user.return_value = zabbix_user_id
        profile = self.UserProfile.get_default()
        profile.user = self.user
        profile.save(username=self.username, raw_password=self.raw_password)
        self.assertEqual(profile.zabbix_user_id, zabbix_user_id)

    def test_default_profile(self, gw):
        profile = self.UserProfile.get_default()
        self.assertIsNotNone(profile.language)
        self.assertIsNone(profile.pk)
        self.assertEqual(profile.language.language_code, settings.LANGUAGE_CODE)
        self.UserLanguage.objects.all().delete()
        self.assertEqual(self.UserLanguage.objects.count(), 0)
        profile = self.UserProfile.get_default()
        self.assertIsNone(profile.language)

    def test_save_profile(self, gw):
        zabbix_user_id = 7
        gw.create_user.return_value = zabbix_user_id
        profile = self.UserProfile.get_default()
        profile.user = self.user
        with self.assertRaises(IntegrityError):
            profile.save()
        profile.save(username=self.username, raw_password=self.raw_password)
        self.assertIsNotNone(profile.pk)
        self.assertEqual(profile.zabbix_user_id, zabbix_user_id)
