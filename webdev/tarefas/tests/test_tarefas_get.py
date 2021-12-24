import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains

@pytest.fixture
def resposta(client):
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

def test_formulario_present(resposta):
    assertContains(resposta, '<form')