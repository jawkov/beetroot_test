from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import TodoList, Task
from .serializers import TodoListSerializer, TaskSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_todo_list(title=""):
        if title != "":
            return TodoList.objects.create(title=title)

    @staticmethod
    def create_task(name="", description="", todo_list=None, status=False):
        if name != "" and todo_list is not None:
            Task.objects.create(
                name=name,
                description=description,
                todo_list=todo_list,
                status=status
            )

    def setUp(self):
        # add test data
        list1 = self.create_todo_list("list1")
        self.create_task("task1", "sth", list1)
        self.create_task("task2", list1)
        self.create_todo_list("list2")


class TasksTest(BaseViewTest):

    def test_get_all_tasks(self):
        """
        This test ensures that all tasks added in the setUp method
        exist when we make a GET request to the tasks/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("tasks")
        )
        # fetch the data from db
        expected = Task.objects.all()
        serialized = TaskSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoListTest(BaseViewTest):

    def test_get_all_todo_lists(self):
        """
        This test ensures that all todo_lists added in the setUp method
        exist when we make a GET request to the tasks/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("todos")
        )
        # fetch the data from db
        expected = TodoList.objects.all()
        serialized = TodoListSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

