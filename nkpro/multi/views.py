from django.shortcuts import render


videos = [
    {'slug': 'infomoney', 'titulos': 'InfoMoney', 'vimeo_id': 'BtAS8nqLMig'},
    {'slug': 'sebrae', 'titulos': 'Sebrae', 'vimeo_id': 'QlnThFtNDDc'},
]


videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'multi/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'multi/video.html', context={'video': video})
