from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_no = models.IntegerField(default=0)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(default=0)

    objects = models.Manager() # manager 'objects' is the link in models and database

    def __str__(self):
        return self.title
