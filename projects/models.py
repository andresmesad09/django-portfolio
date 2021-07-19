from django.db import models

# Create your models here.
class Project(models.Model):
    # Django create an id automatically
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/projects/img')
