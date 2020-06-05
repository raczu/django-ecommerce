from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'