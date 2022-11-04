from rest_framework import serializers

from mainapp.models import*


class research_JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = research_Job
        fields = "__all__"

# class research_ApplicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JobApplication
#         fields = "__all__"


class catagaries_formSerializer(serializers.ModelSerializer):

    class Meta:
        model = catagaries_form
        fields = "__all__"

