from django.contrib import admin
from django.urls import path
from home import views




urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
]
