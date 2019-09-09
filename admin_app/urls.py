from django.contrib import admin
from django.urls import path, re_path
from admin_app import views


app_name='admin_app'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^donor/',views.donor,name='donor'),
    re_path(r'^waitlist/',views.waitlist,name='waitlist'),
    re_path(r'^check/',views.check,name='check'),

]

