from django.urls import path

from .views import (
    TodoItemCreateView,
    TodoItemDeleteView,
    TodoItemToggleView,
    TodoListCreateView,
    TodoListDeleteView,
    TodoListDetailView,
    TodoListView,
)

app_name = "todo"
urlpatterns = [
    path("list", TodoListView.as_view(), name="list"),
    path("create", TodoListCreateView.as_view(), name="create_list"),
    path("list/delete/<int:pk>", TodoListDeleteView.as_view(), name="delete_list"),
    path("item/delete/<int:pk>", TodoItemDeleteView.as_view(), name="delete_item"),
    path("item/toggle/<int:pk>", TodoItemToggleView.as_view(), name="toggle_item"),
    path("<slug:slug>/create", TodoItemCreateView.as_view(), name="create_item"),
    path("<slug:slug>", TodoListDetailView.as_view(), name="detail"),
]
