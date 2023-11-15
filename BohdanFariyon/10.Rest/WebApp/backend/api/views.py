from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo
# Create your views here.

class TodoList(generics.ListAPIView):

    serializer_class = TodoSerializer
    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(user=user).order_by('-created')


class TodoListCreate(generics.ListCreateAPIView):

    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = TodoSerializer
     permission_classes = [permissions.IsAuthenticated]
     def get_queryset(self):
         user = self.request.user

         return Todo.objects.filter(user=user)
