from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        messages.success(self.request, 'Регистрация прошла успешно.')

        return response
