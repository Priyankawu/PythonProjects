from django.db import models

name_choices={
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
}


# Create your models here.
class User(models.Model):
    prefix = models.CharField(max_length=10, default='',choices=name_choices)
    firstname = models.CharField(max_length=60, default='', blank=True)
    lastname = models.CharField(max_length=60, default='', blank=True)
    email = models.CharField(max_length=30, default='', blank=True)
    username = models.CharField(max_length=60, default='', blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.firstname

