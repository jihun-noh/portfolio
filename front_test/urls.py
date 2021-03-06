"""MyBuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map),
    path('login/', views.login),
    path('menu/', views.menu),
    path('signup/', views.signup),
    path('changeprofile/', views.change_profile),
    path('updateobs/', views.update_obs),
    path('diveloglist/', views.dive_log_list),
    path('divelogform/', views.dive_log_form),
]
