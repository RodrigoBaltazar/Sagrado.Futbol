from django.shortcuts import render
from django.template import loader

from .models import Video


def index(request):
    latest_videos_list = Video.objects.order_by('-pub_date')[:5]
    template = loader.get_template('futebol/index.html')
    context = {
        'latest_videos_list': latest_videos_list,
    }
    return render(request, 'futebol/index.html', context)