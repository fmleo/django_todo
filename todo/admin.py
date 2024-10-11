from django.contrib import admin

from .models import TodoItem, TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_at", "updated_at"]
    list_filter = ["owner"]


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["description", "completed", "list"]
    list_filter = ["completed", "list"]
