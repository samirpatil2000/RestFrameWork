from django.urls import path

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('',views.createPost,name='add'),

]
