from django.urls import path
from .views import ToDoListView, ToDoDetailView

urlpatterns = [
    path('todos/', ToDoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', ToDoDetailView.as_view(), name='todo-detail'),
]
