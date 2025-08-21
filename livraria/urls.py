from django.urls import path
from . import views

app_name = 'livraria'

urlpatterns = [
    path('', views.livro_lista, name='livro_lista'),
    path('livros/novo/', views.livro_criar, name='livro_criar'),
    path('livros/<int:pk>/', views.livro_detalhe, name='livro_detalhe'),
    path('livros/<int:pk>/editar/', views.livro_editar, name='livro_editar'),
    path('livros/<int:pk>/excluir/', views.livro_excluir, name='livro_excluir'),
    path('teste/', views.livro_teste, name='livro_teste'),
]
