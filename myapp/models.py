from django.db import models

# Create your models here.
# models.py

from django.db import models

class JobDescription(models.Model):
    job_role = models.CharField(max_length=50)
    company_description = models.TextField()
    role_description = models.TextField()
    qualification = models.TextField()
    Experience = models.IntegerField()

    def __str__(self):
        return self.job_role

class Skill(models.Model):
    job_description = models.ForeignKey(JobDescription, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
