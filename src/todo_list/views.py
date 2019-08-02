from .models import TodoList, Task
from .serializers import TodoListSerializer, TaskSerializer
from rest_framework import viewsets, decorators, status
from rest_framework.response import Response


class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @decorators.action(detail=False, methods=['post'], url_path='finish_task')
    def finish_task(self, request, *args, **kwargs):
        task_id = request.data.get('id')

        task = Task.objects.filter(id=task_id).first()
        if task and not task.is_done:
            task.is_done = True
            task.save()

        return Response(status=status.HTTP_201_CREATED)

