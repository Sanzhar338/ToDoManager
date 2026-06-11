from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=False,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'field-control',
            'placeholder': 'Введите email',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'field-control',
                'placeholder': 'Введите имя пользователя',
            }),
        }

        labels = {
            'username': 'Имя пользователя',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'field-control',
            'placeholder': 'Введите пароль',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'field-control',
            'placeholder': 'Повторите пароль',
        })

        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Повтор пароля'
