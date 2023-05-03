from rest_framework import serializers
from .models import Ozer, TotalOzer

class OzerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ozer
        fields = '__all__'
        
class TotalOzerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TotalOzer
        fields = '__all__'