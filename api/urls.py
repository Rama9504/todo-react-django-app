from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from . import views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('tasks/delete_all/', views.delete_all_tasks, name='delete_all_tasks'),
]
