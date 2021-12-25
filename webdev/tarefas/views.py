from django.shortcuts import render
from django.http import HttpResponse
from webdev.forms import TarefaNovaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from webdev.tarefas.models import Tarefa


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes}, status=400)
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    return render(request, 'tarefas/home.html',{'tarefas_pendentes': tarefas_pendentes})

def detalhe(request, tarefa_id):
    return None