#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('apresentacao', views.apresentacao_view, name='apresentacao'),
    path('cadeiras/<int:id>', views.cadeira_view, name='cadeira'), 
    path('edita-cadeira/<int:cadeira_id>', views.edita_cadeira_view, name='editar_cadeira'),
    path('apaga-cadeira/<int:cadeira_id>', views.apaga_cadeira_view, name='apagar_cadeira'),
    path('nova-cadeira/', views.nova_cadeira_view, name='novo_cadeira'),

    path('projetos', views.projetos_view, name='projetos'),
    path('edita-projeto/<int:projeto_id>', views.edita_projeto_view, name='editar_projeto'),
    path('apaga-projeto/<int:projeto_id>', views.apaga_projeto_view, name='apagar_projeto'),
    path('novo-projeto/', views.novo_projeto_view, name='novo_projeto'),

    path('edita-tfc/<int:tfc_id>', views.edita_tfc_view, name='editar_tfc'),
    path('apaga-tfc/<int:tfc_id>', views.apaga_tfc_view, name='apagar_tfc'),
    path('novo-tfc/', views.novo_tfc_view, name='novo_tfc'),

    path('web', views.web_view, name='web'),
    path('descricaoWeb/<int:id>', views.descricaoWeb_view, name='descricaoWeb'),
    path('quizz', views.quizz_view, name='quizz'),
    path('blog', views.blog_view, name='blog'), 
    path('contactos', views.contactos_view, name='contactos'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)