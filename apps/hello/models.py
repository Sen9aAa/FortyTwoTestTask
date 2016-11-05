from django.db import models


class MyInfo(models.Model):
	name = models.CharField(max_length = 200)
	surname = models.CharField(max_length = 200)
	contacts = models.EmailField(max_length = 200)
	bio = models.TextField(blank = True)
	birthday = models.DateField()

