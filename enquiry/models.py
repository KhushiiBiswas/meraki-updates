from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=15)
    message = models.TextField(max_length=800)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.date} | {self.name} | {self.mobile} | {self.email}'
