from django.contrib.auth import views
from django.urls import path

from users.forms import LoginForm, CustomPasswordChangeForm
from users.forms import CustomPasswordResetForm, CustomSetPasswordForm
from users.views import singup, user_list, user_detail, profile

app_name = 'users'

urlpatterns = [
    path('login/',
         views.LoginView.as_view(template_name='users/login.html',
                                 authentication_form=LoginForm),
         name='login'),
    path('logout/',
         views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
    path('password_change/',
         views.PasswordChangeView.as_view(template_name='users/password_change.html',
                                          form_class=CustomPasswordChangeForm),
         name='password_change'),
    path('password_change/done/',
         views.PasswordChangeDoneView.as_view(template_name='users/password_changed.html')),
    path('reset_password/',
         views.PasswordResetView.as_view(template_name='users/reset_password.html',
                                         form_class=CustomPasswordResetForm),
         name='reset_password'),
    path('password_reset/done/',
         views.PasswordResetDoneView.as_view(template_name='users/reset_mail_send.html'),
         name='reset_mail_send'),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html',
                                                form_class=CustomSetPasswordForm),
         name='reset_password_confirm'),
    path('reset/done/',
         views.PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'),
         name='reset_password_done'),
    path('singup/',
         singup, name='singup'),
    path('user_list/',
         user_list, name='user_list'),
    path('user_detail/<pk>/',
         user_detail, name='user_detail'),
    path('profile/',
         profile, name='profile'),
]
