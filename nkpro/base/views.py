# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from nkpro.modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
