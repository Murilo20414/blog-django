from django.conf.urls import url
from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('accounts/logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
]