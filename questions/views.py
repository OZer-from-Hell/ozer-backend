from . import serializers
from .models import Qustions
from list.models import List
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework import exceptions, decorators, permissions, status
from datetime import datetime
# Create your views here.

class QustionView(APIView) :

    def get(self, request):
        list_id = request.GET.get('list_id', None)
        try:
            List.objects.get(id=list_id)
        except List.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data='This list does not exist')
            
        try:
            questions = Qustions.objects.filter(list=list_id).order_by("order")  
            serializer = serializers.QustionSerializer(questions, many = True)  
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Qustions.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'error':'this question does not exist'})
            

        
        
        
        