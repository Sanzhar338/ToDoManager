from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm

class UserTaskQuerySetMixin:
    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

class TaskListView(LoginRequiredMixin, UserTaskQuerySetMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tasks = super().get_queryset()

        query = self.request.GET.get('q')
        status = self.request.GET.get('status')
        sort = self.request.GET.get('sort')

        tasks = tasks.search(query)

        if status == 'completed':
            tasks = tasks.completed()
        elif status == 'active':
            tasks = tasks.active()

        if sort == 'oldest':
            tasks = tasks.order_by('created_at')
        elif sort == 'title':
            tasks = tasks.order_by('title')
        else:
            tasks = tasks.order_by('-created_at')

        return tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['query'] = self.request.GET.get('q')
        context['status'] = self.request.GET.get('status')
        context['sort'] = self.request.GET.get('sort')

        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserTaskQuerySetMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task_list')
    pk_url_kwarg = 'task_id'

class TaskDeleteView(LoginRequiredMixin, UserTaskQuerySetMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
    pk_url_kwarg = 'task_id'
