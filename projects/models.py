from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="pictures/projectImages", blank=True, null=True)

    def __str__(self):
        return self.title
