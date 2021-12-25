import pytest
from django.urls import reverse
from webdev.tarefas.models import Tarefa

@pytest.fixture
def tarefa_pendente(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=True)

@pytest.fixture
def resposta_com_tarefa(client, tarefa):
    resp = client.post(reverse('tarefas:detalhe', kwargs ={'tarefa_id': tarefa.id}),
                       )
    return resp