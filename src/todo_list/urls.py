from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todo-list', views.TodoListViewSet, base_name='todos')
router.register('task', views.TaskViewSet, base_name='tasks')
urlpatterns = router.urls
