from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class Registration(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label='Имя пользователя')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label='Фамилия')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}), label='Подтвердите пароль')

    error_messages = {
        'password_mismatch': "Пароли не совпадают"
    }
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'Поле "{fieldname}" обязательно'.format(
                fieldname=field.label)}
        