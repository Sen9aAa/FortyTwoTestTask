from django.core.management.base import BaseCommand
from django.db import models
import sys

class Command(BaseCommand):
	def handle(self, *args, **options):
		all_models = models.get_models()
		for c in range(len(all_models)):
		    model_name = all_models[c]._meta.object_name
		    model_objects = all_models[c].objects.count()
		    z = 'Model name %s has %s objects'%(model_name,model_objects)           
		    print(z)
		    print >> self.stderr,'error : '+z



