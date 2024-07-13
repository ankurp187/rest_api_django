from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Todo
from .serializers import TodoSerializer


class TodoListApiView(APIView):

    # add permissions to check if user is Authenticated
    permission_classes = [permissions.IsAuthenticated]


    def get(self,request,*args,**kwargs):
        '''List all the Todo items for given requested user'''
        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        '''Create the Todo with given todo data'''
        data = {
            'task': request.data.get('task'),
            'completed':request.data.get('completed'),
            'user':request.user.id
        }

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    




