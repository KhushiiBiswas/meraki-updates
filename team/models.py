from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='teamphotos',default='default.jpg')

    def __str__(self):
        return self.name
