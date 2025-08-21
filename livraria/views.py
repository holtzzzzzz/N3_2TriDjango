from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Livro
from .forms import LivroForm

# LISTA: Mostrar todos os livros
def livro_lista(request):
    livros = Livro.objects.all().order_by('titulo')
    return render(request, 'livraria/livro_list.html', {'livros': livros})

# CREATE: Criar novo livro
def livro_criar(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livraria:livro_lista')
    else:
        form = LivroForm()
    return render(request, 'livraria/livro_form.html', {
        'form': form,
        'titulo_pagina': 'Adicionar Livro'
    })

# DETALHE: Mostrar informações de um livro específico
def livro_detalhe(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livraria/livro_detail.html', {'livro': livro})

# UPDATE: Editar livro existente
def livro_editar(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livraria:livro_detalhe', pk=livro.pk)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livraria/livro_form.html', {
        'form': form,
        'livro': livro,
        'titulo_pagina': 'Editar Livro'
    })


# DELETE: Excluir livro
def livro_excluir(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':  # Só deleta se for POST
        livro.delete()
        return redirect('livraria:livro_lista')
    # Se for GET, mostra a página de confirmação
    return render(request, 'livraria/livro_deletar.html', {'livro': livro})


# TESTE: Apenas para verificar se o app está funcionando
def livro_teste():
    return HttpResponse('<h1>Teste da Livraria</h1>')
