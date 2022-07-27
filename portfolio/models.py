from statistics import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length =64)
    linkPaginaLusofona = models.URLField(default = "",blank = True)
    linkPaginaLinkedin = models.URLField(default = "", blank = True)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length = 64)
    ano = models.IntegerField(default = 1)
    semestre = models.IntegerField(default = 1, choices = [(1, "semestre 1"), (2, "semestre 2"),(3, "anual")])
    ects = models.IntegerField(default = 6, validators = [MinValueValidator(limit_value = 1), MaxValueValidator(limit_value = 20)])
    anoLetivoFrequentado = models.IntegerField(default = 2020)
    topicosAbordados = models.CharField(default = "", blank = True, max_length = 1024)
    ranking = models.IntegerField(default = 3, choices = [(1, "1 estrela"), (2, "2 estrelas"),(3, "3 estrelas"), (4, "4 estrelas"), (5, "5 estrelas")])
    linkCadeira = models.URLField(default = "", blank = True)
    professores = models.ManyToManyField(Pessoa, blank = True)
    
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length = 64)
    descricao = models.CharField(default = "", blank = True, max_length = 500)
    imagem = models.ImageField(default = "", blank = True)
    anoRealizacao = models.IntegerField(default = 2020)
    cadeira = models.ForeignKey(Cadeira, null = True, blank = True, on_delete = models.SET_NULL)
    participantes = models.ManyToManyField(Pessoa, blank = True)

    def __str__(self):
        return self.titulo
    

class Formacao(models.Model):
    curso = models.CharField(max_length = 64)
    local = models.CharField(default = "", blank = True, max_length = 64)
    periodo = models.DateField(blank = True)
    logotipo = models.ImageField(blank = True)

    def __str__(self):
        return self.curso


class Competencia(models.Model):
    titulo = models.CharField(max_length = 64)
    descricao = models.CharField(default = "", blank = True, max_length = 512)
    projetos = models.ManyToManyField(Projeto, blank = True)
    disciplinaAplicada = models.ManyToManyField(Cadeira, blank = True)
    tecnologies = models.CharField(default = "", blank = True, max_length = 512)
    linguas = models.CharField(default = "", blank = True, max_length = 512)

    def __str__(self):
        return self.titulo


class Interesse(models.Model):
    titulo = models.CharField(max_length = 64)
    descricao = models.CharField(default = "", blank = True, max_length = 512)
    fotografia = models.ImageField(blank = True)
    link = models.URLField(blank = True)

    def __str__(self):
        return self.titulo


class Tecnologia(models.Model):
    nome = models.CharField(max_length = 64)
    acronimo = models.CharField(max_length = 64)
    anoDeCriacao = models.IntegerField(default = 1950, validators = [MinValueValidator(limit_value = 1900), MaxValueValidator(limit_value = 2022)])
    criador = models.CharField(max_length = 64)
    descricao = models.CharField(max_length = 512)
    siteOficial = models.URLField(default = "", blank = True)
    logotipo = models.ImageField(default = "", blank = True)

    def __str__(self):
        return self.nome

class Tfc(models.Model):
    titulo = models.CharField(max_length = 64)
    autor = models.ManyToManyField(Pessoa, blank = True, related_name='tfc_autor')
    orientador = models.ManyToManyField(Pessoa, blank = True, related_name='tfc_orientador')
    anoRealizacao = models.IntegerField(default = 2020)
    sumario = models.CharField(max_length = 64, blank = True)
    resumo = models.CharField(max_length = 500, blank = True)
    linkRelatorio = models.URLField(default = "", blank = True)
    linkGitHub = models.URLField(default = "", blank = True)
    videoYouTube = models.URLField(default = "", blank = True) 

    def __str__(self):
        return self.titulo
        

class Noticia(models.Model):
    titulo = models.CharField(max_length = 64)
    texto = models.CharField(max_length = 256)
    foto = models.ImageField(default = "", blank = True)
    link = models.URLField(default = "", blank = True)
    
    def __str__(self):
        return self.titulo


class Post(models.Model):
    autor = models.CharField(max_length = 64)
    titulo = models.CharField(max_length = 64)
    descricao = models.CharField(max_length = 256)
    link = models.URLField(default = "", blank = True)
    foto = models.ImageField(default = "", blank = True)

    def __str__(self):
        return self.titulo


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length = 64)
    pontuacao = models.IntegerField(default = 0)

    def __str__(self):
        return self.nome
