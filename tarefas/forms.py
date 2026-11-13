from django import forms
from .models import Usuario, Tarefa


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome', 'email']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
        }


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['usuario', 'descricao', 'setor', 'prioridade']

        widgets = {
            'usuario': forms.Select(attrs={
                'class': 'form-select'
            }),
            'descricao': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'setor': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


class AtualizarTarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['status', 'prioridade']

        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-select'
            }),
        }