from django import forms
from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'description': 'Post'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo do post'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do conteúdo'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'}),
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'description': 'Descrição'
        }

    nome = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo do post'})
    ano = forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1})
    descricao = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'})
    docente_teorica = forms.ModelChoiceField(queryset = Cadeira.professores.objects.all())
    docentes_praticas = forms.ModelChoiceField(queryset = Cadeira.professores.objects.all())
    projetos = forms.ModelChoiceField(queryset=Projeto.objects.all())
    classificacao = forms.NumberInput(attrs={'class': 'form-control', 'max': 5, 'min': 1})


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'description': 'Descrição'
        }

    nome = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'})
    ano = forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1})
    descricao = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição'})
    image = forms.ImageField


class AutorForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'description': 'Descrição'
        }

    nome = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'})


class TfcForm(ModelForm):
    class Meta:
        model = Tfc
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'description': 'Descrição'
        }

    nome = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'})
    autores = forms.ModelMultipleChoiceField(queryset=Tfc.autor.objects.all())
    orientadores = forms.ModelMultipleChoiceField(queryset=Cadeira.professores.objects.all())
    ano = forms.ImageField()
    titutlo = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo'})
    description = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'})
    link = forms.URLField()
    linkgithub= forms.URLField()