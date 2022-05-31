from django.contrib import admin
from .models import Cadeira, Competencia, Formacao, Interesse, Projeto, Pessoa, Tecnologia,Noticia, Post

# Register your models here.

admin.site.register(Cadeira)
admin.site.register(Projeto)
admin.site.register(Pessoa)
admin.site.register(Competencia)
admin.site.register(Formacao)
admin.site.register(Interesse)
admin.site.register(Tecnologia)
admin.site.register(Noticia)
admin.site.register(Post)