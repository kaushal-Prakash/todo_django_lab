from django.db import models

class Project(models.Model):
    topic = models.CharField(max_length=100)  # Field for the project topic
    languages_used = models.TextField()  # Field for languages used
    duration = models.PositiveIntegerField()  # Field for project duration in weeks

    def __str__(self):
        return self.topic
