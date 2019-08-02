from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Task(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    # if false - not done, if true - done
    is_done = models.PositiveSmallIntegerField(default=False)

    def __str__(self):
        return self.name
