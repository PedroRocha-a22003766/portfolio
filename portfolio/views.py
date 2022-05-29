from django.shortcuts import render
from .models import Cadeira, Pessoa, Projeto, Competencia, Tecnologia, Perfil

# Create your views here.

def home_page_view(request):
	return render(request, 'portfolio/home.html')


def apresentacao_view(request):
	cadeiras = Cadeira.objects.all()

	map = {
		'ano1': {
			'semestre1': [],
			'semestre2': []
		},
		'ano2': {
			'semestre1': [],
			'semestre2': []
		},
		'ano3': {
			'semestre1': [],
			'semestre2': [],
			'semestre3': []
		}
	}

	for cadeira in cadeiras:
		map["ano" + str(cadeira.ano)]['semestre' + str(cadeira.semestre)].append(cadeira)
		
	return render(request, 'portfolio/apresentacao.html', {'mapa': map})


def cadeira_view(request, id):
	cadeira = Cadeira.objects.get(pk = id)
	projetos = Projeto.objects.filter(cadeira = id)

	return render(request, 'portfolio/cadeira.html', {'cadeira': cadeira, 'projetos': projetos, 'professores' : cadeira.professores.all() })


def projetos_view(request):
	projetos = Projeto.objects.all()

	return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def web_view(request):
	tecnologias = Tecnologia.objects.all()

	return render(request, 'portfolio/web.html', {'tecnologias': tecnologias})

def descricaoWeb_view(request):
	tecnologia = Tecnologia.objects.all()
	
	return render(request, 'portfolio/descricaoWeb.html', {'tecnologia': tecnologia})


def blog_view(request):
	return render(request, 'portfolio/blog.html')


def sobre_view(request):
	return render(request, 'portfolio/sobre.html')


def contactos_view(request):
	perfis = Perfil.objects.all()

	return render(request, 'portfolio/contactos.html', {'perfis': perfis})

