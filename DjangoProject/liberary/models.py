from django.db import models

class Writer(models.Model):

    witer_name = models.CharField(max_length=200)
    # date_birth= models.DateTimeField(default='')
    # date_death=models.DateTimeField(default='')
    # Contact=models.URLField(blank=True)
    # Bio=models.TextField(blank=True)
    #
    def __str__(self):
        return self.witer_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    date_publish= models.DateTimeField(default='')
    sammary=models.TextField(blank=True)
    country= models.TextField(blank=True)
    link = models.URLField(blank=True)
    Writer = models.ForeignKey(Writer,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.title



    class Meta:
        ordering =['title']
