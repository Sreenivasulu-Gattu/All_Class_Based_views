from django.db import models

# Create your models here.
from django.urls import reverse

class School(models.Model):
    sname = models.CharField(max_length = 100)
    sprinc = models.CharField(max_length  =100 )
    sloc = models.CharField(max_length  = 100)

    def get_absolute_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})


    def __str__(self):
        return self.sname
    
class Student(models.Model):
    sname = models.ForeignKey(School,on_delete = models.CASCADE,related_name = 'students')
    stdname = models.CharField(max_length = 100)
    stdage = models.IntegerField()