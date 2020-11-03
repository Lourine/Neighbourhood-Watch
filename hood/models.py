from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt

Priority=(
    ('Informational','Informational'),
    ('High Priority','High Priority'),
)

# Create your models here.
class neighbourhood(models.Model):
    neighbourhood= models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()


class notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15,choices=Priority,default="Informational")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,healthservices):
        cls.objects.filter(healthservices=healthservices).delete()


class Business(models.Model):
    name =models.CharField(max_length=100)
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='businesslogo/')
    email = models.EmailField()
    address =models.CharField(max_length=100)
    phone_number= models.CharField(max_length=10, blank=True)

    @classmethod
    def search_business(cls,searched_business):
        business = cls.objects.filter(name__icontains=searched_business)
        return business
    def __str__(self):
        return self.name

class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/', blank = True)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address =models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name

class Authorities(models.Model):
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default= 'user')
    email = models.CharField(max_length=100, default='null')
    Location = models.CharField(max_length=200)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.username
