from django.urls import path, re_path
from . import views

# reverse(), namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('drinks/<str:drink_name>/', views.drinks, name='drinks'),
    re_path(r'^noms/s(?P<nom_name>\S+)/$', views.noms, name='noms'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('booking/', views.form_view),
]