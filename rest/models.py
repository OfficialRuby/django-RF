from django.db import models
from django.conf import settings


class User(models.Model):
    name = models.CharField(max_length=50)
    usename = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField()
    location = models.CharField(max_length=30)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
