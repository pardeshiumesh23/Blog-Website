from django.urls import path
from . import views
from django.contrib.auth import views as auth_view #django default views for login and logout operations
urlpatterns=[
    path('sign_up/',views.sign_up,name='users-signup'),
    path('profile/',views.profile,name='users-profile'),
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='users-login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='users-logout'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'), #this will provide a form to us and after entering mail id a mail will be sent on our mail id
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'), #it will flash a msg that password reset is done
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

]   