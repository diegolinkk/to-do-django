from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.tarefas,name='tarefas'),
    path('tarefas/<int:categoria_id>/',views.tarefas_por_categoria,name='tarefas_por_categoria'),
    path('concluir_tarefa/<int:tarefa_id>/',views.concluir_tarefa,name='concluir_tarefa'),
    path('cadastrar_tarefa/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path('cadastrar_categoria/',views.cadastrar_categoria,name='cadastrar_categoria'),
 ]