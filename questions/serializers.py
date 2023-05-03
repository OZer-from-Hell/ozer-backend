from rest_framework import serializers
from .models import Qustions

class QustionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qustions
        fields = ('order', 'content', 'answer', 'no1', 'no1','no2','no3','no4',)