from django.shortcuts import render, get_object_or_404
from nkpro.multi.models import Video


def indice(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'multi/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'multi/video.html', context={'video': video})
