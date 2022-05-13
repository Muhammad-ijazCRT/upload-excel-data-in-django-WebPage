from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class UploadCsv(models.Model):
    textfile = models.ImageField(upload_to='files')
