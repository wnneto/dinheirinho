import pytest
from django.urls import reverse

from nkpro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('multi:video', args=('infomoney',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):  # Teste para o título da página
    assert_contains(resp, 'InfoMoney' or 'Sebrae')


def test_conteudo_video(resp):  # Teste para o título da página
    assert_contains(resp, 'src="https://www.youtube.com/embed/BtAS8nqLMig"')
