from multiprocessing import context
from django.shortcuts import render
from .models import Cadeira, Pessoa, Projeto, Formacao, Competencia, Tecnologia, Post, Interesse, Noticia

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
	
	competencias = Competencia.objects.all()
	interesses = Interesse.objects.all()
	formacoes = Formacao.objects.all()

	context = {'mapa': map, 'competencias': competencias,'interesses': interesses,'formacoes': formacoes}
		
	return render(request, 'portfolio/apresentacao.html', context)


def cadeira_view(request, id):
	cadeira = Cadeira.objects.get(pk = id)
	projetos = list(Projeto.objects.filter(cadeira = id))
	context = {'cadeira': cadeira, 'projetos': projetos, 'professores' : cadeira.professores.all() }

	return render(request, 'portfolio/cadeira.html', context)


def projetos_view(request):
	projetos = Projeto.objects.all()
	context = {'projetos': projetos}

	return render(request, 'portfolio/projetos.html', context)


def web_view(request):
	tecnologias = Tecnologia.objects.all()
	noticias = Noticia.objects.order_by('?')[:10]
	context = {'tecnologias': tecnologias, 'noticias' : noticias}

	return render(request, 'portfolio/web.html', context)

def descricaoWeb_view(request, id):
	tecnologia = Tecnologia.objects.get(pk = id)
	context = {'tecnologia': tecnologia}
	
	return render(request, 'portfolio/descricaoWeb.html', context)


def blog_view(request):
	posts = Post.objects.order_by('?')[:6]
	context = {'posts': posts}	

	return render(request, 'portfolio/blog.html', context)


def sobre_view(request):
	return render(request, 'portfolio/sobre.html')


def contactos_view(request):
	return render(request, 'portfolio/contactos.html')

