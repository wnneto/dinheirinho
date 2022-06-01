import pytest
# from django.test import Client
from django.urls import reverse

from nkpro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):   # Teste de resposta
    assert resp.status_code == 200


def test_title(resp):   # Teste para testar o título da página
    assert_contains(resp, '<title>Dinheirinho Smart Gestão!</title>')


def test_home_link(resp):   # Teste home link
    assert_contains(resp, f'href="{reverse("base:home")}">Home</a>')
