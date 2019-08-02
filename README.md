Create venv:

```sh
$ python3 -m venv ./env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

Django:
```sh
$ ./src/manage.py createsuperuser // create admin
$ ./src/manage.py migrate // apply database changes
$ ./src/manage.py runserver
```

API
```sh
http://127.0.0.1:8000/api/task/ -- GET all tasks
http://127.0.0.1:8000/api/task/ -- POST(name and todo_list(use todo_list_id) are required) to create task
http://127.0.0.1:8000/api/task/finish_task/ -- POST(pass task_id to body) to finish task
http://127.0.0.1:8000/api/task/{id}/ -- PATCH to update task
http://127.0.0.1:8000/api/task/{id}/ -- DELETE task

http://127.0.0.1:8000/api/todo-list/ -- GET all todo-lists
http://127.0.0.1:8000/api/todo-list/ -- POST(title is required) to create todo-list
http://127.0.0.1:8000/api/todo-list/{id}/ -- PATCH to update todo-list
http://127.0.0.1:8000/api/todo-list/{id}/ -- DELETE todo-list
```