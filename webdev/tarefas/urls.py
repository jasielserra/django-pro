from django.urls import path, include

app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home')
]