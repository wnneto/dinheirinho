import pytest
# from django.test import Client
from django.urls import reverse
from model_bakery import baker

from nkpro.django_assertions import assert_contains
from nkpro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp


def test_title_modulo(resp, modulos):   # Teste para o título da página
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_link_modulo(resp, modulos):   # Teste para o título da página
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())
