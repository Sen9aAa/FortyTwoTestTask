from django.test import TestCase
from django.test import Client
from apps.hello.models import MyInfo
from datetime import date
from django.core.urlresolvers import reverse

# Create your tests here.


class SomeTests(TestCase):
    def create_instance_model(self):
        self.info = MyInfo.objects.create(name = 'Test',surname = 'Only a test',
                                    contacts = "test@gmail.com",birthday = date(1990,02,21))
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)
    
    def test_template(self):
        self.client = Client()
        response = self.client.get('/')
        return self.assertEqual(response.status_code,200)

    def test_models(self):
        self.create_instance_model()
        return self.assertEqual(MyInfo.objects.all().count(),1)

    def test_views(self):
        self.create_instance_model()
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.info.name,response.content)