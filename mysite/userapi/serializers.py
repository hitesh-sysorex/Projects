from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import userData

class userDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = userData
        fields = '__all__'