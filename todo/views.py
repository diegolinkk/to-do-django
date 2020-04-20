from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Categoria,Tarefa
from .forms import TarefaForm, CategoriaForm

#como muitos lugares carregam isso, virou função
def carregar_categorias():
    C = Categoria.objects.all()
    return C

def tarefas(request):
    tarefas = Tarefa.objects.order_by('feito')
    categorias = carregar_categorias()
    return render(request,'todo/tarefas.html',{'categorias':categorias, 'tarefas': tarefas})

def tarefas_por_categoria(request,categoria_id):
    categorias = carregar_categorias()

    #usei 0 no index para puxar todas as categorias
    if categoria_id==0:
        return redirect('tarefas')

    C = Categoria.objects.get(id=categoria_id)
    tarefas = C.tarefa_set.all() #tarefas por categoria
    return render(request,'todo/tarefas.html',{'categorias':categorias,'tarefas':tarefas})

def concluir_tarefa(request,tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.feito = True
    tarefa.save()
    return redirect('tarefas')


def cadastrar_tarefa(request):

    if request.method=='POST':
        f = TarefaForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('tarefas')


    categorias = carregar_categorias()
    form = TarefaForm()
    return render(request,'todo/cadastrar_tarefa.html',{'form':form,'categorias': categorias})

def cadastrar_categoria(request):

    if request.method == 'POST':
        f = CategoriaForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('tarefas')

    categorias = carregar_categorias()
    form = CategoriaForm()
    return render(request,'todo/cadastrar_categoria.html',{'form':form,'categorias':categorias})


def excluir_tarefa(request, tarefa_id):
    t = Tarefa.objects.get(id=tarefa_id)
    t.delete()
    return redirect('tarefas')