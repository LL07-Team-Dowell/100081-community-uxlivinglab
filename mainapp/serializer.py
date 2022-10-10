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

class CountrySerializer(serializers.ModelSerializer):
    job = JobSerializer(many=True)
    class Meta:
        model = Country
        fields = ['Country_name', 'job']

    def create(self, validated_data):
        jobs_data = validated_data.pop('job')
        country = Country.objects.create(**validated_data)
        for job_data in jobs_data:
            Job.objects.create(country=country, **job_data)
        return country





class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"