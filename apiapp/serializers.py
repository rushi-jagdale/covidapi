from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Hospital


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'        