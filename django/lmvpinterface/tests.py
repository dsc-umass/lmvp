from django.test import TestCase

# Create your tests here.
class AlwaysFailsTestCase(TestCase):
    def failingTest(self):
        self.assertEqual(True, False)
