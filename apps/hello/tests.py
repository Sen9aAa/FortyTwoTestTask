from django.test import TestCase
from django.test import Client

# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)
    
    def test_template(self):
    	self.client = Client()
    	response = self.client.get('/')
    	return self.assertEqual(response.status_code,200)
