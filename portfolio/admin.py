from django.contrib import admin
from .models import Cadeira, Projeto, Pessoa
# Register your models here.

admin.site.register(Cadeira)
admin.site.register(Projeto)
admin.site.register(Pessoa)