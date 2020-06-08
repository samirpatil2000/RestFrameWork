from django.urls import path

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.home,name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='MainApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='MainApp/logout.html'), name='logout')

]
