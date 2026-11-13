from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):

    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS_CHOICES = [
        ('a fazer', 'A fazer'),
        ('fazendo', 'Fazendo'),
        ('pronto', 'Pronto'),
    ]

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='tarefas'
    )

    descricao = models.CharField(max_length=255)
    setor = models.CharField(max_length=100)

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES
    )

    data_cadastro = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='a fazer'
    )

    def __str__(self):
        return self.descricao