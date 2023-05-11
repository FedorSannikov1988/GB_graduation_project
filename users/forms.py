from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms

'''
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
'''


# или другой вариант:

class UserLoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(
            label="Логин",
            widget=forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Имя пользователя'})
        )

    password = forms.CharField(
            max_length=25,
            label="Пароль",
            widget=forms.PasswordInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Пароль'})
        )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
