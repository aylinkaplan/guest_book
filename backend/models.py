from django.db import models


class GuestBook(models.Model):

    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
