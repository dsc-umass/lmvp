from django.test import TestCase, RequestFactory #we may migrate to the DRF test utilities in the future
#from rest_framework.test import APIRequestFactory #this is provided by DRF for testing
from django.utils import timezone
from .models import *
from os import path
# Create your tests here.
class TautologyTestCase(TestCase):
    def test_true(self):
        self.assertEqual(True, True)
class RetrievalTestCase(TestCase):
    def setUp(self):
        Project.objects.create(name="TestProject")
        User.objects.create(username="hpotter", created=timezone.now())
        Commit.objects.create(author=User.objects.get(username="hpotter"), project=Project.objects.get(name="TestProject"),
        hash=0b1001011010100011010111011001011010011110110110110, created=timezone.now())
    def test_retrieve_user(self):
        request = self.factory.get('/users')
        request.user = AnonymousUser() #TODO complete this test
    def test_retrieve_commit(self):
        pass #TODO complete this test
class StaticFormTestCase(TestCase):
    def test_static_form_present(self):
        self.assertEqual(os.path.exists('management/commands/genforms.py'))
