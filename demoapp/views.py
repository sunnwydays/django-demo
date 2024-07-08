from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import BookingForm
from .models import Menu

# class-based views?? mixins??

def home(request):
    return render(request, 'home.html')

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
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, 'about.html', {'content': about_content})

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {'menu': menu_items}
    return render(request, 'menu.html', items_dict)

def book(request):
    return HttpResponse('Make a booking')

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)