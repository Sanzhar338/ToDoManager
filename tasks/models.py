from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class TaskQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(user=user)

    def completed(self):
        return self.filter(is_completed=True)

    def active(self):
        return self.filter(is_completed=False)

    def search(self, query):
        if not query:
            return self

        return self.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )


class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskQuerySet.as_manager()

    def __str__(self):
        return self.title