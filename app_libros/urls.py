from django.urls import path
from app_libros import views


urlpatterns = [
    path('',views.inicio),
    path('autores/', views.ver_autores),
    path('libros/', views.ver_libros),
]
