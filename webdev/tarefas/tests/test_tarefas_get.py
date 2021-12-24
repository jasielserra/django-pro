from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains

def test_status_code(client: Client):
    resposta = client.get(reverse('tarefas:home'))
    assert resposta.status_code == 200

def test_formulario_present(client):
    resposta = client.get(reverse('tarefas:home'))
    assertContains(resposta, '<form')