import pytest
from django.urls import reverse
from model_bakery import baker

from nkpro.django_assertions import assert_contains
from nkpro.multi.models import Video


@pytest.fixture
def video(db):
    return baker.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('multi:video', args=(video.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture
def resp_video_off(client, video):
    return client.get(reverse('multi:video', args=(video.slug + 'video_nao_existe',)))


def test_status_code_video_off(resp_video_off):
    # Teste para links offline
    assert resp_video_off.status_code == 404


def test_title_video(resp, video):
    # Teste para o título da página
    assert_contains(resp, video.titulos)


def test_conteudo_video(resp, video):
    # Teste para link do video
    assert_contains(resp, f'<iframe src="https://www.youtube.com/embed/{video.yt_id}"')
