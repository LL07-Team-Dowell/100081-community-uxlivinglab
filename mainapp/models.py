from django.db import models

# Create your models here.
class CommunityTable(models.Model):
    
    Age = models.CharField(max_length=100)
    Gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("other", "other"),
       
    )

    Gender = models.CharField(max_length=50, choices=Gender_choices)
    Qualification_choices = Gender_choices = (
        ("Master's Degree", "Master's Degree"),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Higher Secondary School", "Higher Secondary School"),
        ("Secondary School", "Secondary School"),
        ("No Formal Schooling", "No Formal Schooling"),
        ("Other", "Other"),
       
    )
    qualification = models.CharField(max_length=100, choices=Qualification_choices)
    income_choices = (
        ("Low income", "Low income"),
        ("Middle income", "Middle income"),
        ("High income", "High income"),
       
    )

    income = models.CharField(max_length=50, choices=income_choices)
    Occupation = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    Name_suggestion = models.CharField(max_length=100)
    Other = models.JSONField()
    def __str__(self):
        return str(self.id) 

    
    
    