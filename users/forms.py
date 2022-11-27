from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
        )
