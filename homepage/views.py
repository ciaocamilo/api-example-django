from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='text-align: -webkit-center;font-family: system-ui;color: darkorange;'>Bienvenido a la API de Prueba</h1>")

# Create your views here.
