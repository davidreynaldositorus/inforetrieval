from django.conf.urls import url
from django.contrib import admin
from searching import views
from django.urls import path


app_name = 'searching'
urlpatterns = [
    path('',views.index),
    path('result/',views.result),

]
