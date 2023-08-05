from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField()
    applied_in_companies = models.IntegerField(default=0)
    shortlisted=models.IntegerField(default=0)
    rejected = models.IntegerField(default=0)
    in_process = models.IntegerField(default=0)

    def __str__(self):
        return self.username
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=10, unique=True)
    enroll = models.CharField(max_length=20, default='register now')

    def __str__(self):
        return self.course_name
