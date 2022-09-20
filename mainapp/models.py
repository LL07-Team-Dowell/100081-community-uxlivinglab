from django.db import models

# Create your models here.
class job(models.Model):
    
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
    PENDING = 0
    DONE = 1
    income = models.CharField(max_length=50, choices=income_choices)
    Occupation = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    Name_suggestion = models.CharField(max_length=100)
    status = models.CharField(max_length=132, null=True, default="Pending")
    Other = models.JSONField()
    def __str__(self):
        return str(self.id) 

    
    
class JobApplication(models.Model):
    applicant = models.CharField(max_length=100, null=False)
    job = models.ForeignKey(job, on_delete=models.CASCADE, null=False)
    feedBack = models.TextField(null=True)
    country = models.CharField(max_length=132, null=True)
    hr_remarks = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=132, null=True, default="Pending")
    others = models.JSONField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Job Applications'

    def __str__(self):
        return f'{self.job}-{self.applicant}'