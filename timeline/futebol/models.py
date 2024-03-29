from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('Date Published')
    votes = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    filepath = models.CharField(max_length=200)
    approved = models.BooleanField(default=0)

    def __str__(self):
        return self.name