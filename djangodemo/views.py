# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1>')

def handler404(request, exception):
    # return render(request, 'poo.html', status=404)
    return HttpResponse('404 error 📰', status=404)

