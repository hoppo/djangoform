from django.db import models

# Create your models here.

class Report(models.Model):
    event = models.CharField(max_length=60,null=True,blank=True)
    author = models.CharField(max_length=40,null=True,blank=True)
    datetime = models.DateTimeField(null=True,blank=True) 
    diagnosis = models.TextField(null=True,blank=True) 
    impact = models.TextField(null=True,blank=True)
    resolution = models.TextField(null=True,blank=True)
    responsibility = models.TextField(null=True,blank=True)
    actionable = models.NullBooleanField(null=True,blank=True)
    action = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return self.event

    class Meta:
        ordering = ['datetime']
