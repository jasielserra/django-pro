from django.shortcuts import render
from django.http import HttpResponse
from webdev.forms import TarefaNovaForm
# Create your views here.



def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tarefas/home.html')