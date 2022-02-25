from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class user(models.Model):
    STATUS = (
        (1, 'activated'),
        (0, 'in_activated'),

    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS, default=0)
    job = models.ForeignKey('job', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class job(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=255, null=True)
    salary = models.PositiveIntegerField()
    brief_intro = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey('industry', null=True, on_delete=models.SET_NULL)
    skill = models.ManyToManyField('skill')

    def __str__(self):
        return self.title


class industry(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


























