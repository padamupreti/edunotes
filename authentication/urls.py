from django.urls import path

from .views import login_or_register, logout_user

app_name = 'authentication'
urlpatterns = [
    path('login-or-register/', login_or_register, name='login-or-register'),
    path('logout-user/', logout_user, name='logout-user'),
]
