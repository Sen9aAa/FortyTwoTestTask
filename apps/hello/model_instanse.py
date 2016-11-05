from .models import MyInfo
from datetime import date

def create_instanse():
    info = MyInfo.objects.create(name = 'Test',surname = 'Only a test',
                                contacts = "test@gmail.com",
                                birthday = date(1990,02,21))
    return info

                                
                                
                                
                                
