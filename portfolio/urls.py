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
    path('projetos', views.projetos_view, name='projetos'),
    path('web', views.web_view, name='web'),
    path('descricaoWeb/<int:id>', views.descricaoWeb_view, name='descricaoWeb'),
    path('quizz', views.quizz_view, name='quizz'),
    path('blog', views.blog_view, name='blog'), 
    path('contactos', views.contactos_view, name='contactos'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)