from django.shortcuts import render
from django.http import HttpResponse, Http404

# class-based views?? mixins??

def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1>')

def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
    }
    try:
        choice_of_drink = drink[drink_name]
    except:
        raise Http404('Drink not found')
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)

def noms(request, nom_name):
    return HttpResponse(f"<h2 style=\"background-color:#b0fffb;\"> The part after the starting s is: {nom_name} </h2>")

def about(request):
    return HttpResponse('About us')

def menu(request):
    return HttpResponse('Menu')

def book(request):
    return HttpResponse('Make a booking')