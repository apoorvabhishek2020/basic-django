from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        "title": "Basic Django App",
        "top_header": "Basic Django Application",
        "body_header": "Django Application",
        "body_description": "This is the Basic Django Application for testing workflows",
    }
    return render(request, 'preview/home.html', context)
