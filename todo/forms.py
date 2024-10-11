from crispy_forms.helper import FormHelper
from django.forms.models import ModelForm

from .models import TodoItem, TodoList


class CreateTodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ["title"]

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = self.owner
        if commit:
            instance.save()
        return instance


class CreateTodoItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "description",
        ]

    def __init__(self, *args, **kwargs):
        self.list = kwargs.pop("list")
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def save(self, commit=True):
        instance: "TodoItem" = super().save(commit=False)
        instance.list = self.list
        if commit:
            instance.save()
        return instance
