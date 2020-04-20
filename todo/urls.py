from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.tarefas,name='tarefas'),
    path('tarefa/<int:categoria_id>/',views.tarefas_por_categoria,name='tarefas_por_categoria'),
    path('tarefa/concluir/<int:tarefa_id>/',views.concluir_tarefa,name='concluir_tarefa'),
    path('tarefa/cadastrar/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path('tarefa/excluir/<int:tarefa_id>/',views.excluir_tarefa, name='excluir_tarefa'),
    path('categoria/cadastrar/',views.cadastrar_categoria,name='cadastrar_categoria'),
 ]