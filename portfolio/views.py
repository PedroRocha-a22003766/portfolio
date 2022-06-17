from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Cadeira, Pessoa, Projeto, Formacao, Competencia, Tecnologia, Post, Interesse, Noticia, PontuacaoQuizz, Tfc

# Create your views here.
def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username = username,
            password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {'message': 'Credenciais invalidas.'})

    return render(request, 'portfolio/login.html')

def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html', {'message': 'Foi desconetado.'})


@login_required	
def home_page_view(request):
	return render(request, 'portfolio/home.html')


@login_required
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

@login_required
def projetos_view(request):
	projetos = Projeto.objects.all()
	tfcs = Tfc.objects.all()
	context = {'projetos': projetos, 'tfcs' : tfcs}

	return render(request, 'portfolio/projetos.html', context)


@login_required
def web_view(request):
	tecnologias = Tecnologia.objects.all()
	noticias = Noticia.objects.order_by('?')[:10]
	context = {'tecnologias': tecnologias, 'noticias' : noticias}

	return render(request, 'portfolio/web.html', context)


def descricaoWeb_view(request, id):
	tecnologia = Tecnologia.objects.get(pk = id)
	context = {'tecnologia': tecnologia}
	
	return render(request, 'portfolio/descricaoWeb.html', context)


def quizz_view(request):
	if request.method == 'POST':
		n = request.POST['nome']
		#p = pontuacao_quizz(request)
		#r = PontuacaoQuizz(nome=n, pontuacao=p)
		#r.save()

	return render(request, 'portfolio/quizz.html')


def blog_view(request):
	posts = Post.objects.order_by('?')[:6]
	context = {'posts': posts}	

	return render(request, 'portfolio/blog.html', context)


@login_required
def contactos_view(request):
	return render(request, 'portfolio/contactos.html')
