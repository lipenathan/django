import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from hello_world.forms import LogMessageForm
from django.shortcuts import redirect
from hello_world.models import LogMessage
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import  generic


# Create your views here.

def home(request):
    # return HttpResponse("Olá Mundo!")
    return render(request, "hello_world/home.html")

def sobre(request):
    return render(request, "hello_world/sobre.html")

def contato(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.log_date = datetime.now()
            mensagem.save()
            return redirect("home")
    else:
        return render(request, "hello_world/contato.html", {"form":form})

def ola_campeao(request, nome):
    texto = f"Olá {nome}! Tu é um campeão"
    return HttpResponse(texto)


def ola(request, nome):
    return render(
        request, 'hello_world/ola.html',
        {
            'nome' : nome,
            'data' : datetime.now(),
        }
    )

def mensagens(request):
    return render(
        request, 'hello_world/mensagens.html')

class MensagensListView(ListView):
    model = LogMessage
    def get_context_data(self, **kwargs):
        context = super(MensagensListView, self).get_context_data(**kwargs)
        return context

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"