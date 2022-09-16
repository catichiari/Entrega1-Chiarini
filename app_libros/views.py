from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from app_libros.models import Autor, Libro

def inicio (request):
    return render (request, 'app_libros/inicio.html')

def ver_autores (request):
    return render (request, 'app_libros/autores.html')

def ver_libros (request):
    return render (request, 'app_libros/libros.html')

