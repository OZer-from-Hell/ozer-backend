from rest_framework import serializers
from .models import Ozer

class OzerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ozer
        fields = '__all__'