from django import forms
from .models import Tarefa, Categoria

class TarefaForm(forms.ModelForm):

    class Meta():
        model = Tarefa
        fields = ['nome','data','feito','categoria']

class CategoriaForm(forms.ModelForm):
    
    class Meta():
        model = Categoria
        fields = ['nome']