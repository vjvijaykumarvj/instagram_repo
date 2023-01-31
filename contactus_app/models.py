from django.db import models
from django.core.validators import RegexValidator

course = (('Python','Python'),('Java','Java'),('C++','C++'),('Selenium','Selinium'),('Django','Django'))
trining = (('Online','Online'),('Offline','Offline'))

phone_regex = RegexValidator(regex="[0-9]{10}",message='Please Enter Valid Mobile Number')

class ContactUS(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.name


class Blog_model(models.Model):
    name = models.CharField(max_length=256)
    phonenumber = models.CharField(max_length=10,validators=[phone_regex])
    email = models.EmailField()
    selectcourse = models.CharField(max_length=10,choices=course)
    modeloftrining = models.CharField(max_length=20,choices=trining)
