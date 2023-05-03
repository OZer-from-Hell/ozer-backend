from . import serializers
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework import exceptions, decorators, permissions, status
from datetime import datetime
from .models import TotalOzer, Ozer
from questions.models import Qustions
from list.models import List


class OzerView(APIView) :
    
    def get(self, request):
        list_id = request.GET.get('list_id', None)
        try:
            List.objects.get(id=list_id)
        except List.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data='This list does not exist')
        
        total_ozer = Ozer.objects.filter(list = list_id).order_by('-score')
        serializer = serializers.OzerSerializer(total_ozer, many = True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        if not 'nickname' in request.data:
            return Response(data={'error':'nickname is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = serializers.OzerSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        try:
            total_ozer = TotalOzer.objects.get(list_id = request.data['list'])
            total_ozer.number += 1
            total_ozer.save()
            
        except:
            TotalOzer.objects.create(list_id = request.data['list'], number = 1)
        
        
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
       
    def patch(self, request):
        if not 'user_id' in request.data or not 'answers' in request.data:
            return Response(data={'error': 'user_id and answers are required'}, status=status.HTTP_400_BAD_REQUEST)
            
        user_id = request.data['user_id']
        try:
            ozer = Ozer.objects.get(id = user_id)
            list = ozer.list_id
        except Ozer.DoesNotExist:
            return Response(data={'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        copy_data =  request.data.copy()
        total_question = Qustions.objects.filter(list = list).all()
        if len(request.data['answers']) != len(total_question):
            return Response(data={'error':'답안지의 길이가 문제수와 일치하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)
        score = int(100 * request.data['answers'].count('1')/len(total_question))
        copy_data['score'] = score 
        serializer = serializers.OzerSerializer(ozer, copy_data, partial=True)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
            
# class Score(APIView) :

#     def post(self, request):
        
# class Ranking(APIView) :

#     def get(self, request):
