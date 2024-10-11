from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from todo.forms import CreateTodoItemForm
from todo.models import TodoItem, TodoList


class TodoItemCreateView(LoginRequiredMixin, View):
    model = TodoItem

    form_class = CreateTodoItemForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST, list=TodoList.objects.get(slug=kwargs["slug"])
        )
        if form.is_valid():
            form.save()
            return render(
                request, "todo/partials/item_entry.html", {"item": form.instance}
            )

        return HttpResponse(status=400)


class TodoItemDeleteView(LoginRequiredMixin, View):
    model = TodoItem

    def get(self, request, pk, *args, **kwargs):
        todo_item = self.model.objects.get(pk=pk, list__owner=request.user)
        todo_item.delete()
        return HttpResponse(status=200)


class TodoItemToggleView(LoginRequiredMixin, View):
    model = TodoItem

    def post(self, request, pk, *args, **kwargs):
        todo_item = self.model.objects.get(pk=pk, list__owner=request.user)
        todo_item.completed = not todo_item.completed
        todo_item.save()
        return HttpResponse(status=200)
