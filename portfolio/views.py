from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import Cadeira, Pessoa, Projeto, Formacao, Competencia, Tecnologia, Post, Interesse, Noticia, PontuacaoQuizz, Tfc
from .forms import CadeiraForm, ProjetoForm

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


@login_required
def edita_cadeira_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(id = cadeira_id)
    form = CadeiraForm(request.POST or None, instance = cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:cadeira'))

    context = {'form': form, 'cadeira_id': cadeira_id}

    return render(request, 'portfolio/editar_cadeira.html', context)


@login_required
def apaga_cadeira_view(request, cadeira_id):
    Cadeira.objects.get(id = cadeira_id).delete()

    return HttpResponseRedirect(reverse('portfolio:cadeira'))


def nova_cadeira_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:cadeira'))

    context = {'form': form}

    return render(request, 'portfolio/nova_cadeira.html', context)


def projetos_view(request):
	projetos = Projeto.objects.all()
	tfcs = Tfc.objects.all()

	context = {'projetos': projetos, 'tfcs' : tfcs}

	return render(request, 'portfolio/projetos.html', context)


@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id = projeto_id)
    form = ProjetoForm(request.POST or None, instance = projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}

    return render(request, 'portfolio/editar_projeto.html', context)


@login_required
def apaga_projeto_view(request, projeto_id):
    Projeto.objects.get(id = projeto_id).delete()

    return HttpResponseRedirect(reverse('portfolio:projetos'))


def novo_projeto_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    form = ProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/novo_projeto.html', context)


@login_required
def edita_tfc_view(request, tfc_id):
    tfc = Tfc.objects.get(id = tfc_id)
    form = ProjetoForm(request.POST or None, instance = tfc)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'tfc_id': tfc_id}

    return render(request, 'portfolio/editar_tfc.html', context)


@login_required
def apaga_tfc_view(request, tfc_id):
    Tfc.objects.get(id = tfc_id).delete()

    return HttpResponseRedirect(reverse('portfolio:projetos'))


def novo_tfc_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    form = ProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/novo_projeto.html', context)


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
    p = 0

    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome = n, pontos = p)
        r.save()
        desenha_grafico_resultados(r)

    context = {'pontos': p}

    return render(request, 'portfolio/quizz.html', context)


def pontuacao_quizz(request):
    pontos = 0
    form = request.POST

    if form['p1'] == 'Python':
        pontos += 1

    if form['p2'] == 'Web2py':
        pontos += 1

    if form['p3'] == '1995':
        pontos += 1

    if form['p4'] == 'Boa navegação':        
	     pontos += 1

    ##if form['p5'] == 'marcação':
        ##pontos += 1

    ##if form['p6'] == '53':
        ##pontos += 1	

	##if form['p7'] == '<iframe>':
        ##pontos += 1
	
    ##return pontos


def desenha_grafico_resultados():
    pontuacoes = sorted(PontuacaoQuizz.objects.all(), key=lambda x: x.pontos, reverse=True)

    pessoas_x = []
    pontos_y = []

    for resposta in pontuacoes:
        pessoas_x.append(resposta.nome)
        pontos_y.append(resposta.pontos)

    pessoas_x.reverse()
    pontos_y.reverse()


def blog_view(request):
	posts = Post.objects.order_by('?')[:6]
	context = {'posts': posts}	

	return render(request, 'portfolio/blog.html', context)


def contactos_view(request):
	return render(request, 'portfolio/contactos.html')
