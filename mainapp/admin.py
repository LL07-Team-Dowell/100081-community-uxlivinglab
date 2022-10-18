from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(
    [
        community
    ])
admin.site.register(
    [
        Country
    ])
admin.site.register(
    [
        Job
    ])
admin.site.register(
    [
        JobApplication
    ])
admin.site.register(
    [
        jobCatagaries
    ])
admin.site.register(
    [
        catagaries_form
    ])
