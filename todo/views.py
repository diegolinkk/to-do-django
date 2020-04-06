from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria



def index(request):
    categorias = Categoria.objects.all()
    return render(request,'todo/tarefas.html',{'categorias':categorias})


# Create your views here.
