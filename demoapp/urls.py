from django.urls import path, re_path
from . import views
from .views import IndexView

# reverse(), namespace

urlpatterns = [
    # path('', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('', IndexView.as_view(), name='home'),
    path('drinks/<str:drink_name>/', views.drinks, name='drinks'),
    re_path(r'^noms/s(?P<nom_name>\S+)/$', views.noms, name='noms'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('booking/', views.form_view),
]