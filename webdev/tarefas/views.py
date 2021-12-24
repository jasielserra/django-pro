from django.shortcuts import render
from django.http import HttpResponse
from webdev.forms import TarefaNovaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.



def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas/home.html', {'form': form}, status=400)
    return render(request, 'tarefas/home.html')