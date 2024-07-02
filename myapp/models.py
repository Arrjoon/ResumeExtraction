from django.db import models

# Create your models here.
# models.py

class Job_Description(models.Model):
    job_role = models.CharField(max_length=50)
    company_description = models.TextField()
    role_description = models.TextField()
    qualification = models.TextField(null=True)
    degree = models.CharField(max_length=100,null=True)
    experience = models.IntegerField()
    skills = models.TextField(help_text="Comma-separated list of skills")
    def __str__(self):
        return self.job_role
    def get_skills_list(self):
        return self.skills.split(',')





class Resume_Description(models.Model):
    name = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    email_address = models.EmailField(null=True)
    company_working_at = models.CharField(max_length=100,null=True)
    degree = models.CharField(max_length=100,null=True)
    college_name = models.CharField(max_length=100,null=True)
    graduation_year = models.CharField(max_length=20,null=True)
    experience = models.CharField(max_length=20,null=True)
    university = models.CharField(max_length=25,null=True)
    skills = models.TextField(help_text="Comma-separated list of skills")

    def __str__(self):
        return self.name

    def get_skills_list(self):
        return self.skills.split(',')