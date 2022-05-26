from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=64)
    linkPaginaLusofona = models.URLField(default="",blank=True)
    linkPaginaLinkedin = models.URLField(default="", blank=True)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length = 64)
    ano = models.IntegerField(default = 1)
    semestre = models.IntegerField(default = 1, choices = [(1, "semestre 1"), (2, "semestre 2"),(3, "anual")])
    ects = models.IntegerField(default = 6, validators = [MinValueValidator(limit_value=1), MaxValueValidator(limit_value=20)])
    anoLetivoFrequentado = models.IntegerField(default = 2020)
    topicosAbordados = models.CharField(default = "",blank = True, max_length = 1024)
    ranking = models.IntegerField(default = 3, choices = [(1, "1 estrela"), (2, "2 estrelas"),(3, "3 estrelas"), (4, "4 estrelas"), (5, "5 estrelas")])
    linkCadeira = models.URLField(default = "", blank = True)
    professores = models.ManyToManyField(Pessoa)
    
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length = 64)
    descricao = models.CharField(max_length = 500)
    imagem = models.ImageField()
    anoRealizacao = models.IntegerField(default = 2020)
    cadeira = models.ForeignKey(Cadeira, null = True, blank = True, on_delete = models.SET_NULL)
    participantes = models.ManyToManyField(Pessoa)

    def __str__(self):
        return self.titulo
    

class Competencia(models.Model):
    titulo = models.CharField(max_length = 64)
    descricao = models.CharField(max_length = 512)
    projetos = models.ForeignKey(Projeto, null = True, blank = True, on_delete = models.SET_NULL)
    disciplinaAplicada = models.ForeignKey(Cadeira, null = True, blank = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.titulo


class Interesses(models.Model):
    titulo = models.CharField(max_length = 64)
    descricao = models.CharField(max_length = 512)
    fotografia = models.ImageField(default = "")

    def __str__(self):
        return self.titulo
    