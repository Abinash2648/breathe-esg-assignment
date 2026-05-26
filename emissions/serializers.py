from rest_framework import serializers

from .models import *


class EmissionRecordSerializer(serializers.ModelSerializer):

    class Meta:

        model = EmissionRecord

        fields = '__all__'