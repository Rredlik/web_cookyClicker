from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import TextInput, Textarea, EmailInput
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=_(""),
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'email',
            'placeholder': 'Введите никнейм'
        }),
    )

    email = forms.EmailField(
        label=_(""),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'autocomplete': 'email',
            'placeholder': 'example@mail.ru'
        }),
    )

    password1 = forms.CharField(
        label=_(""),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            "autocomplete": "new-password",
            'placeholder': 'Введите пароль'
        }),
        help_text=_("<br>"),
    )

    password2 = forms.CharField(
        label=_(""),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            "autocomplete": "new-password",
            'placeholder': 'Подтвердите пароль'
        }),
        strip=False,
        help_text=_(""),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
        label = _(""),
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите никнейм'
            })
        }


class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'placeholder': 'никнейм'
    }))
    password = forms.CharField(
        label=_(""),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }