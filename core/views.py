from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from usuarios.forms import CustomUsuarioCreateForm
from usuarios.models import CustomUsuario
from django.contrib import messages


def registrar(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST
        print(form)
        # check whether it's valid:
        """
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('index/')
        """
    # if a GET (or any other method) we'll create a blank form
    """
    else:
        form = CustomUsuario()
    """
    return render(request, 'register.html')


class MyFormView(View):
    form_class = CustomUsuarioCreateForm
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})





