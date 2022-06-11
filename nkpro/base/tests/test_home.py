import pytest
# from django.test import Client
from django.urls import reverse

from nkpro.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):   # Teste de resposta
    assert resp.status_code == 200


def test_title(resp):   # Teste para o título da página
    assert_contains(resp, '<title>Dinheirinho - Home</title>')


def test_home_link(resp):   # Teste home link
    assert_contains(resp, f'href="{reverse("base:home")}"><b>Home</b></a>')


def test_email_link(resp):   # Teste email link
    assert_contains(resp, 'href="mailto:wn.nt3w@gmail.com"')
