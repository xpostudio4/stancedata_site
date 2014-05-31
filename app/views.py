#Django imports
from events.functions import get_updated_event_list
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'site/index.html')

def about(request):
    return render(request, 'site/about.html')

def careers(request):
    return render(request, 'site/careers.html')

def leadership(request):
    return render(request, 'site/leadership.html')

def community(request):
    return render(request, 'site/community.html')

def news(request):
    try:
        main_event = get_updated_event_list()[0]
    except IndexError:
        main_event = []

    return render(request, 'site/news.html',{
        'main_event':main_event,
        'event_list': get_updated_event_list()[1:] })
