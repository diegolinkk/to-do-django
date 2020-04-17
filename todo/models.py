from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'


class Tarefa(models.Model):
    nome = models.CharField(max_length=250)
    data = models.DateTimeField() #data para conclusão
    feito = models.BooleanField(default="False")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.categoria}'