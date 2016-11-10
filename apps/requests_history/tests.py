from django.test import TestCase
from django.test import Client


class SomeTest2(TestCase):
    
    def test_template(self):
        self.client = Client()
        response = self.client.get('/request_history')
        return self.assertEqual(response.status_code,200)

