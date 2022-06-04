import pytest
from django.urls import reverse

from nkpro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('multi:video', args=('InfoMoney',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):  # Teste para o título da página
    assert_contains(resp, '<h5 class="card-title"><b>InfoMoney</b></h5>')


def test_conteudo_video(resp):  # Teste para o título da página
    assert_contains(resp, 'src="https://player.vimeo.com/video/577177067"')