from django.contrib import admin
from .models import Cadeira, Competencia, Projeto, Pessoa, Tecnologia, Post
# Register your models here.

admin.site.register(Cadeira)
admin.site.register(Projeto)
admin.site.register(Pessoa)
admin.site.register(Competencia)
admin.site.register(Tecnologia)
admin.site.register(Post)