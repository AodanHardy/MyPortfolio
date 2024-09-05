from datetime import timezone

from django.db import models
from django.utils import timezone


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    display_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
