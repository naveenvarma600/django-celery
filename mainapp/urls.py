from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.test,name='test'),
    path('sendmail/', views.sendmail_toall, name="sendmail"),
]
