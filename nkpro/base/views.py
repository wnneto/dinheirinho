from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('<html><body>NAS NUVENS!!!</body></html>', content_type='text/html')
