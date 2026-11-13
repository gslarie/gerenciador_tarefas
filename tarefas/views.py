from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Usuario, Tarefa
from .forms import UsuarioForm, TarefaForm, AtualizarTarefaForm


def kanban(request):

    tarefas_a_fazer = Tarefa.objects.filter(
        status='a fazer'
    ).select_related('usuario')

    tarefas_fazendo = Tarefa.objects.filter(
        status='fazendo'
    ).select_related('usuario')

    tarefas_prontas = Tarefa.objects.filter(
        status='pronto'
    ).select_related('usuario')

    contexto = {
        'tarefas_a_fazer': tarefas_a_fazer,
        'tarefas_fazendo': tarefas_fazendo,
        'tarefas_prontas': tarefas_prontas,
    }

    return render(request, 'tarefas/kanban.html', contexto)


def cadastrar_usuario(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('cadastrar_usuario')

    else:
        form = UsuarioForm()

    return render(request, 'tarefas/cadastrar_usuario.html', {
        'form': form
    })


def cadastrar_tarefa(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('kanban')

    else:
        form = TarefaForm()

    return render(request, 'tarefas/cadastrar_tarefa.html', {
        'form': form
    })


def atualizar_tarefa(request, id):

    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        form = AtualizarTarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('kanban')

    else:
        form = AtualizarTarefaForm(instance=tarefa)

    return render(request, 'tarefas/atualizar_tarefa.html', {
        'form': form,
        'tarefa': tarefa
    })