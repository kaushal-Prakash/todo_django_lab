from django.db import models

class Course(models.Model):
    coursecode = models.CharField(max_length=20, unique=True)
    coursename = models.CharField(max_length=100)
    credits = models.IntegerField()
    
    def __str__(self):
        return self.coursecode + " - " + self.coursename


class Student(models.Model):
    usn = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.usn + " - " + self.name