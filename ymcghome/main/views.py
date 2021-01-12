from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
from django.utils import timezone
from datetime import datetime, timedelta, date

# Create your views here.\

def index(request):
    footer = Footer.objects.all()[0]
    recruiting_banner = RecruitingBanner.objects.all()[0]
    introduction = Introduction.objects.all()[0]
    youtube = Youtube.objects.all()[0]
    logos = Logo.objects.all().order_by('order')
    key_values = KeyValue.objects.all().order_by('order')[0:3]
    context = {
        'recruiting_banner': recruiting_banner,
        'introduction': introduction,
        'youtube': youtube,
        'logos': logos,
        'key_values': key_values,
        'footer':footer,
    }
    return render(request, 'main/index.html', context)

def about(request):
    footer = Footer.objects.all()[0]
    content = About.objects.all()[0]
    greetings = Greeting.objects.all().order_by('order')

    context = {
        'content': content,
        'footer':footer,
        'greetings': greetings,
    }
    return render(request, 'main/about.html', context)

def activities(request):
    footer = Footer.objects.all()[0]
    content = Activities.objects.all()[0]
    context = {
         'content': content,
         'footer':footer,
    }
    return render(request, 'main/activities.html', context)

def join(request):
    footer = Footer.objects.all()[0]
    content = Join.objects.all()[0]
    recruiting_banner = RecruitingBanner.objects.all()[0]
    context = {
        'recruiting_banner': recruiting_banner,
        'content': content,
        'footer':footer,
    }
    return render(request, 'main/join.html', context)

def elements(request):
    footer = Footer.objects.all()[0]
    elements = Elements.objects.all()[0]

    context = {
        'elements': elements,
        'footer':footer,
    }
    return render(request, 'main/elements.html', context)
