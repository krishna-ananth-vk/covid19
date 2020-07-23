from .models import District, DateReport, TestReport

from rest_framework import serializers

class DistrictSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="cases:district-detail")
    class Meta:
        model = District
        fields = '__all__'