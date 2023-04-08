from . import serializers
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework import exceptions, decorators, permissions, status
from datetime import datetime




class Nickname(APIView) :

    def post(self, request):
        if not 'nickname' in request.data:
            return Response(data={'error':'nickname is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = serializers.OzerSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(data={'success':'nickname was accepted'}, status=status.HTTP_201_CREATED)
       
        
# class Score(APIView) :

#     def post(self, request):
        
# class Ranking(APIView) :

#     def get(self, request):
