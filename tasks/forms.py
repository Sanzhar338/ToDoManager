from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'is_completed')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'field-control',
                'placeholder': 'Введите название задачи',
            }),
            'description': forms.Textarea(attrs={
                'class': 'field-control',
                'placeholder': 'Введите описание задачи',
                'rows': 4,
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'checkbox-control',
            }),
            'priority': forms.RadioSelect(attrs={
                'class': 'priority-input',
            }),
        }

        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'is_completed': 'Выполнена',
            'priority': 'Приоритет',
        }
