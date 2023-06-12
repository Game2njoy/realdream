"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dream import views

urlpatterns = [
    path('', views.index, name='index'),
    path('block5/', views.block5, name='block5'),
    path('block6/', views.block6, name='block6'),
    path('block7/', views.block7, name='block7'),
    path('block8/', views.block8, name='block8'),
    path('block9/', views.block9, name='block9'),
    path('block1/', views.block1, name='block1'),
    path('block4/', views.block4, name='block4'),
]
