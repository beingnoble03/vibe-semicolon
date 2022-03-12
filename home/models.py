from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Detail(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(null = True, blank=True, default="Nothing Here", max_length=100)
    bhawan = models.CharField(default="Nothing Here", max_length=100)
    gender = models.CharField(default="Female", max_length=50)
    country = models.CharField(default="India", max_length=100)
    state = models.CharField(default="Rajasthan", max_length=100)
    zipcode = models.IntegerField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    hobby = models.CharField(max_length=100, null=True, blank=True)
    food = models.CharField(max_length=100, null=True, blank=True)
    hangout = models.CharField(max_length=100, null=True, blank=True)
    music = models.CharField(max_length=100, null=True, blank=True)
    insta = models.TextField(null=True, blank=True, default="")
    facebook = models.TextField(null=True, blank=True, default="")
    twitter = models.TextField(null=True, blank=True, default="")
    image = CloudinaryField('image', null = True)

    def __str__(self):
        return f'{self.username}'

class MatchRequest(models.Model):
    sender = models.CharField(max_length=100, null=True, blank=True)
    getter = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, default="no")

    def __str__(self):
        return f'{self.sender} to {self.getter}'