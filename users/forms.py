from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from core.forms import BaseForm
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginForm(BaseForm, AuthenticationForm):
    pass


class CustomPasswordChangeForm(BaseForm, PasswordChangeForm):
    pass


class CustomPasswordResetForm(BaseForm, PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email,
                                   is_active=True).exists():
            msg = _('К сожалению нам не удалось отправить сообщение')
            self.add_error('email', msg)
        return email


class CustomSetPasswordForm(BaseForm, SetPasswordForm):
    pass


class CustomUserCreationForm(BaseForm, UserCreationForm):
    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        )


class CustomUserChangeForm(BaseForm, UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
            User.birthday.field.name,
        )
