from django.db import models

class email(models.Model):
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
