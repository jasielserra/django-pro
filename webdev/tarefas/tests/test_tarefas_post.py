import pytest
from django.urls import reverse
from webdev.tarefas.models import Tarefa

@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome':'Tarefa'})
    return resp

def test_tarefa_existe_no_bd(resposta):
    assert Tarefa.objects.exists()

@pytest.fixture
def resposta_dado_invalido(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome':''})
    return resp