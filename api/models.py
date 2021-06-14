from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=50)
    school = models.CharField(max_length=200)
    address = models.CharField(max_length=400, null=True)
    maths = models.CharField(max_length=200, null=True)
    sci = models.CharField(max_length=200, null=True)
    eng = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name
