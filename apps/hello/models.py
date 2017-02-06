from django.db import models
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class MyInfo(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    contacts = models.EmailField(max_length = 200, help_text='Please enter your email')
    bio = models.TextField(blank = True)
    birthday = models.DateField()
    photo = models.ImageField(upload_to = 'photos',blank = True,null=True)

    def save(self, *args, **kwargs):
        if self.photo:
            image = Img.open(StringIO.StringIO(self.photo.read()))
            image.thumbnail((200,200), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            name = self.photo.name.split('.')[0]
            output.seek(0)
            self.photo = InMemoryUploadedFile(output,'ImageField', "%s_myfoto.jpg" %name, 'image/jpeg', output.len, None)
        super(MyInfo, self).save(*args, **kwargs)



    def __unicode__(self):
        return '%s %s'%(self.name,self.surname)

