from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import action

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve a single task (GET /api/tasks/<id>/)
    def retrieve(self, request, pk=None, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # Update a task (PUT /api/tasks/<id>/)
    def update(self, request, pk=None, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a task (DELETE /api/tasks/<id>/)
    def destroy(self, request, pk=None, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # List all tasks (GET /api/tasks/)
    def list(self, request, *args, **kwargs):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'], url_path='delete_all')
    def delete_all_tasks(self, request):
        Task.objects.all().delete()  # Delete all tasks
        return Response({"message": "All tasks deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    