from django.db import models
from django.forms import ModelForm
from django.contrib.sites.models import Site

# Create your models here.
class doyouknow(models.Model):
    update_number = models.IntegerField()
    title = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()
    picture = models.FileField(upload_to='/home/pakumar/GuitarClub/guitarchordsapp/static/')
    #sites = models.ManyToManyField(Site)

    def __unicode__(self):
        return self.title