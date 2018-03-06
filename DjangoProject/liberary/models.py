from django.db import models

class Writer(models.Model):
    witer_name = models.CharField(max_length=200)
    date_birth= models.DateTimeField('date Of Birth')
    date_death=models.DateTimeField('date of Death')
    Contact=models.URLField("Enter URL")
    Bio=models.TextField("About")


class Book(models.Model):
    Book_name = models.CharField(max_length=200)
