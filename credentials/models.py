from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Credentials(models.Model):
    url = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    password = models.TextField()
    folder = models.ForeignKey(Folder, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_viewed = models.DateTimeField(auto_now=True)
    password_updated = models.DateTimeField()

    class Meta:
        ordering = ('url',)