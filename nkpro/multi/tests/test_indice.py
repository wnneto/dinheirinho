import pytest
from django.urls import reverse
from model_bakery import baker

from nkpro.django_assertions import assert_contains
from nkpro.multi.models import Video


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('multi:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, videos):
    # Teste para o título da página
    for video in videos:
        assert_contains(resp, video.titulos)


def test_link_video(resp, videos):
    # Teste para o endereço da página
    for video in videos:
        video_link = reverse('multi:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
