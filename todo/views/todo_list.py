from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from todo.forms import CreateTodoItemForm, CreateTodoListForm
from todo.models import TodoList


class TodoListView(LoginRequiredMixin, ListView):
    model = TodoList
    context_object_name = "lists"
    template_name = "todo/list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["add_list_form"] = CreateTodoListForm(user=self.request.user)
        return context

    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user)


class TodoListDetailView(LoginRequiredMixin, DetailView):
    model = TodoList
    context_object_name = "list"
    template_name = "todo/detail.html"
    form_class = CreateTodoItemForm

    def get_object(self, queryset=None):
        return TodoList.objects.get(slug=self.kwargs["slug"], owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_item_form"] = self.form_class(list=self.object)
        return context


class TodoListCreateView(LoginRequiredMixin, View):
    form_class = CreateTodoListForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return render(
                request, "todo/partials/list_entry.html", {"list": form.instance}
            )

        return HttpResponse(status=400)


class TodoListDeleteView(LoginRequiredMixin, View):
    model = TodoList

    def get(self, request, pk, *args, **kwargs):
        todo_list = self.model.objects.get(pk=pk, owner=request.user)
        todo_list.delete()
        return HttpResponse(status=200)
