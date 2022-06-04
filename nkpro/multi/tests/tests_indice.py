import pytest
from django.urls import reverse

from nkpro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('multi:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulos',
    [
        'InfoMoney',
        'Sebrae',

    ]
)
def test_title_video(resp, titulos):
    # Teste para o título da página
    assert_contains(resp, titulos)

# def test_conteudo_video(resp):  # Teste para o título da página
#    assert_contains(resp, 'src="https://player.vimeo.com/video/577177067"')
