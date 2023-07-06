"""
URL configuration for gurutools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from hotel import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('hotel/', views.hotel, name='hotel'),
    path('hotel/create/', views.create_hotel, name='create_hotel'), # <--- Para terminar con el alta de la vista se crea la nueva ruta
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotel/conexion/<int:hotel_id>/', views.conexion, name='conexion'),
    re_path(r'^api/hotel/$', views.hotel_list_a),
    re_path(r'^api/hotel/([0-9])$', views.hotel_detail_a),
]
