from rest_framework import serializers
from .models import Doctor


class Doctorserializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ("user")
