from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.MemberAPI.as_view())
]
