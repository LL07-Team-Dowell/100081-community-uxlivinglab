from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django_countries.fields import CountryField
# Create your models here.

class research_Job(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    skills = models.CharField(max_length=500, null=False, default="None")
    is_active = models.BooleanField(default=False)
    TYPECHOICES = (
        ('Freelancer', 'Freelancer'),
        ('Employee', 'Employee'),
        ('Internship', 'Internship'),
        ('Research Associate', 'Research Associate'),
    )
    typeof = models.CharField(max_length=100, choices=TYPECHOICES, default="Freelance")
    city = models.CharField(max_length=200, null = True)
    location = models.CharField(max_length=132, null=True)
    others = models.JSONField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class JobApplication(models.Model):
#     applicant = models.CharField(max_length=100, null=False)
#     job = models.ForeignKey(research_Job, related_name='jobapplication',  on_delete=models.CASCADE, null=False)
#     # country = models.ForeignKey(Country, related_name='country', on_delete=models.CASCADE, null = True)
#     status = models.CharField(max_length=132, null=True, default="Pending")
#     Age = models.CharField(max_length=100, null= True)
#     Gender_choices = (
#         ("Male", "Male"),
#         ("Female", "Female"),
#         ("other", "other"),
       
#     )

#     Gender = models.CharField(max_length=50, choices=Gender_choices, null = True)
#     Qualification_choices = Gender_choices = (
#         ("Master's Degree", "Master's Degree"),
#         ("Bachelor's Degree", "Bachelor's Degree"),
#         ("Higher Secondary School", "Higher Secondary School"),
#         ("Secondary School", "Secondary School"),
#         ("No Formal Schooling", "No Formal Schooling"),
#         ("Other", "Other"),
       
#     )
#     qualification = models.CharField(max_length=100, choices=Qualification_choices, null = True)
#     income_choices = (
#         ("Low income", "Low income"),
#         ("Middle income", "Middle income"),
#         ("High income", "High income"),
       
#     )
#     PENDING = 0
#     DONE = 1
#     income = models.CharField(max_length=50, choices=income_choices, null = True)
#     Occupation = models.CharField(max_length=100, null = True)
#     others = models.JSONField(null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = 'Job Applications'

#     def __str__(self):
#         return f'{self.job}-{self.applicant}'



class catagaries_form(models.Model):
    email = models.EmailField(unique=True)
    Individual_name = models.CharField(max_length=200)
    Individual_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    phone = models.CharField(null=False, max_length=16, blank=False, unique=True)
