from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1><strong>SORRY TUNT</strong></h1>")
    return render(request, 'preview/home.html', {})
