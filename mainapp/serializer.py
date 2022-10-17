from rest_framework import serializers

from mainapp.models import*

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = community
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class JobApplicationSerializer(serializers.ModelSerializer):
    jobapplication =JobSerializer(many=True)
    class Meta:
        model = JobApplication
        fields = ['applicant', 'jobapplication']

    def create(self, validated_data):
        jobapplications_data = validated_data.pop('jobapplication')
        job = JobApplication.objects.create(**validated_data)
        for job_data in jobapplications_data:
            Job.objects.create(job=job, **job_data)
        return job



class CountrySerializer(serializers.ModelSerializer):
    job = JobSerializer(many=True)
    class Meta:
        model = Country
        fields = ['Country_name', 'city', 'job']

    def create(self, validated_data):
        jobs_data = validated_data.pop('job')
        country = Country.objects.create(**validated_data)
        for job_data in jobs_data:
            Job.objects.create(country=country, **job_data)
        return country


class jobCatagariesSerializer(serializers.ModelSerializer):

    class Meta:
        model = jobCatagaries
        fields = "__all__"


class catagaries_formSerializer(serializers.ModelSerializer):

    class Meta:
        model = catagaries_form
        fields = "__all__"

