

from django.contrib import admin
from django.urls import include, path
from pollingfunction import views

urlpatterns = [
   path('',views.homepage,name='homepage'),
   path('vote/<poll_id>/', views.vote, name='vote'),
   path('result/<poll_id>/', views.result, name='result'),
   path('create/', views.create, name='create'),
]