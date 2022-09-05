from rest_framework import serializers

from mainapp.models import*

class CommunitySerlizer(serializers.ModelSerializer):
    class Meta:
        model = CommunityTable
        fields = "__all__"