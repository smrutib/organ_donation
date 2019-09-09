from django.urls import path
from user_reg import views

urlpatterns = [
    path('',views.form_name_view, name='form_name_view'),
]