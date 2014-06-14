#Django imports
from events.functions import get_updated_event_list
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.views.decorators.http import require_POST
from django.core.mail import send_mail, mail_admins
from django.conf import settings

admin_emails = [ v for k,v in settings.ADMINS]

def home(request):
    form = ContactForm()
    return render(request, 'site/index.html',
            { "contact_form": form})

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

    try:
        event_list = get_updated_event_list()[1:]
    except IndexError:
        event_list = []

    return render(request, 'site/news.html',{
        'main_event':main_event,
        'event_list': event_list  })

@require_POST
def contact(request):
    """This function should process the contact form in the main page and
    return the notification if proccesed correctly"""
    form = ContactForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        send_mail(
                "Contact Info: " + str(data['name']),
                str(data['message']),
                str(data['email']),
                admin_emails,
                fail_silently=False
                )
        return HttpResponse("Form send")
    else:
        return HttpResponse("Form was not validated")
