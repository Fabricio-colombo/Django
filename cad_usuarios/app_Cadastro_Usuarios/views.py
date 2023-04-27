from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a pagina de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)
