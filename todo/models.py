import random
import string

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class TodoItem(models.Model):
    description = models.CharField(verbose_name="Descrição", max_length=64)
    completed = models.BooleanField(verbose_name="Completado", default=False)
    list = models.ForeignKey(
        verbose_name="Lista de tarefas",
        to="todo.TodoList",
        related_name="items",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"


class TodoList(models.Model):
    created_at = models.DateTimeField(verbose_name="Criado em", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="Atualizado em")
    owner = models.ForeignKey(
        verbose_name="Dono",
        to=User,
        related_name="lists",
        on_delete=models.CASCADE,
    )
    title = models.CharField(verbose_name="Título", max_length=64)
    slug = models.SlugField(unique=True, max_length=50, blank=True)

    class Meta:
        verbose_name = "Lista de tarefas"
        verbose_name_plural = "Listas de tarefas"

    @property
    def completed_tasks(self) -> int:
        return self.items.filter(completed=True).count()

    @property
    def formatted_progress(self) -> str:
        return f"{self.completed_tasks}/{self.items.count()}"

    def save(self, *args, **kwargs):
        if not self.slug:
            random_characters = "".join(
                random.choices(string.ascii_letters + string.digits, k=10)
            )
            self.slug = f"{slugify(self.title)[:40]}-{random_characters}"

        self.updated_at = timezone.now()

        super().save(*args, **kwargs)
