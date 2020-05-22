from django.test import TestCase, RequestFactory #we may migrate to the DRF test utilities in the future
#from rest_framework.test import APIRequestFactory #this is provided by DRF for testing
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser
from .models import *
from os import path
import hashlib
# Create your tests here.
class TautologyTestCase(TestCase):
    def test_true(self):
        self.assertEqual(True, True)
class RetrievalTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        test_hash = hashlib.sha1()
        test_hash.update(b'Arbitrary test text')
        Project.objects.create(name="TestProject")
        User.objects.create(username="hpotter", created=timezone.now())
        Commit.objects.create(author=User.objects.get(username="hpotter"), project=Project.objects.get(name="TestProject"),
        hash=test_hash.digest(), created=timezone.now())
    def test_retrieve_user(self):
        request = self.factory.get('/users')
        request.user = AnonymousUser() #TODO complete this test
    def test_retrieve_commit(self):
        pass #TODO complete this test
class StaticFormTestCase(TestCase):
    def test_static_form_present(self):
        self.assertEqual(path.exists('/django/lmvpinterface/management/commands/genforms.py'), True)
