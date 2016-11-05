from django.test import TestCase
from django.test import Client
from apps.hello.models import MyInfo
from datetime import date
# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)
    
    def test_template(self):
    	self.client = Client()
    	response = self.client.get('/')
    	return self.assertEqual(response.status_code,200)

    def test_models(self):
    	info = MyInfo.objects.create(name = 'Test',surname = 'Only a test',
    		                        contacts = "test@gmail.com",birthday = date(1990,02,21))
    	return self.assertEqual(MyI+nfo.objects.all().count(),1)