from django.shortcuts import render
from .models import Cadeira, Pessoa, Projeto

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

	for projeto in projetos:	
		print(projeto)
	return render(request, 'portfolio/projetos.html')


def web_view(request):
	return render(request, 'portfolio/web.html')


def blog_view(request):
	return render(request, 'portfolio/blog.html')


def contactos_view(request):
	return render(request, 'portfolio/contactos.html')


def rodape_view(request):
	return render(request, 'portfolio/rodape.html')

