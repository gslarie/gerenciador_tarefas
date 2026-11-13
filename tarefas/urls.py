from django.urls import path
from . import views

urlpatterns = [
    path('', views.kanban, name='kanban'),

    path(
        'usuarios/cadastrar/',
        views.cadastrar_usuario,
        name='cadastrar_usuario'
    ),

    path(
        'tarefas/cadastrar/',
        views.cadastrar_tarefa,
        name='cadastrar_tarefa'
    ),

    path(
        'tarefas/atualizar/<int:id>/',
        views.atualizar_tarefa,
        name='atualizar_tarefa'
    ),
]