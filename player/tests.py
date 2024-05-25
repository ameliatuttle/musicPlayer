# tests.py
from django.test import TestCase
from django.urls import reverse

# A simple test to verify that someone can access the main page successfully
class SimpleTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)