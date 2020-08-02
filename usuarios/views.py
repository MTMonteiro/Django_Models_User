from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from usuarios.forms import CustomUsuarioCreateForm
from usuarios.models import CustomUsuario
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = CustomUsuarioCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta Criada com sucesso!')
            return HttpResponseRedirect('/')

    else:
        form = CustomUsuarioCreateForm()
    return render(request, 'register.html', {'form': form})

# Form pode ser passado automaticamente para o html usando {{% form %}}
