from rest_framework import serializers

from mainapp.models import*

class CommunitySerlizer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "__all__"

class JobApplicationSerlizer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"