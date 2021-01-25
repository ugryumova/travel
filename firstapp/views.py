from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import tour, hotel, transport_type, price_list, punkt, user
from .forms import Addtour, Addhotel, Addtransport_type, Addprice_list, Addpunkt, Adduser
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from firstapp import forms

def great(request):
    return render(request, "great.html")

def index(request):
    return render(request, "index.html")

def index_tour(request):
    form_tour = Addtour()
    data = tour.objects.all()
    return render(request, "firstapp/Template_tour.html", {"form":form_tour, "data_show":data})

def index_hotel(request):
    form_hotel = Addhotel()
    data = hotel.objects.all()
    return render(request, "firstapp/Template_hotel.html", {"form":form_hotel, "data_show":data})

def index_transport_type(request):
    form_transport_type = Addtransport_type()
    data = transport_type.objects.all()
    return render(request, "firstapp/Template_transport_type.html", {"form":form_transport_type, "data_show":data})

def index_price_list(request):
    form_price_list = Addprice_list()
    data = price_list.objects.all()
    return render(request, "firstapp/Template_price_list.html", {"form":form_price_list, "data_show":data})

def index_punkt(request):
    form_punkt = Addpunkt()
    data = punkt.objects.all()
    return render(request, "firstapp/Template_punkt.html", {"form":form_punkt, "data_show":data})

def index_user(request):
    form_user = Adduser()
    data = user.objects.all()
    return render(request, "firstapp/Template_user.html", {"form":form_user, "data_show":data})

#Определение view

class view_tour(View):
    def add_tour(request):
        if request.method == "POST":
            Tour = tour()
            Tour.type = request.POST.get("type")
            Tour.duration = request.POST.get("duration")
            Tour.save()
            return HttpResponseRedirect("/tour")

    def del_tour(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = tour.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/tour")

    def update_tour(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = tour.objects.get(id=q)
            que.type = request.POST.get("type")
            que.duration = request.POST.get("duration")
            que.save()
            return HttpResponseRedirect("/tour")

class view_hotel(View):
    def add_hotel(request):
        if request.method == "POST":
            Hotel = hotel()
            Hotel.name = request.POST.get("name")
            Hotel.stars = request.POST.get("stars")
            Hotel.save()
            return HttpResponseRedirect("/hotel")

    def del_hotel(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = hotel.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/hotel")

    def update_hotel(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = hotel.objects.get(id=q)
            que.name = request.POST.get("name")
            que.stars = request.POST.get("stars")
            que.save()
            return HttpResponseRedirect("/hotel")

class view_transport_type(View):
    def add_transport_type(request):
        if request.method == "POST":
            Transport_type = transport_type()
            Transport_type.model = request.POST.get("model")
            Transport_type.number_of_places = request.POST.get("number_of_places")
            Transport_type.id_price_list = price_list.objects.get(id=request.POST.get("id_price_list"))
            Transport_type.save()
            return HttpResponseRedirect("/transport_type")

    def del_transport_type(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = transport_type.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/transport_type")

    def update_transport_type(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = transport_type.objects.get(id=q)
            que.model = request.POST.get("model")
            que.number_of_places = request.POST.get("number_of_places")
            que.id_price_list = price_list.objects.get(id=request.POST.get("id_price_list"))
            que.save()
            return HttpResponseRedirect("/transport_type")

class view_price_list(View):
    def add_price_list(request):
        if request.method == "POST":
            Price_list = price_list()
            Price_list.data_of_start = request.POST.get("data_of_start")
            Price_list.cost = request.POST.get("cost")
            Price_list.id_hotel = hotel.objects.get(id=request.POST.get("id_hotel"))
            Price_list.id_tour = tour.objects.get(id=request.POST.get("id_tour"))
            Price_list.save()
            return HttpResponseRedirect("/price_list")

    def del_price_list(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = price_list.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/price_list")

    def update_price_list(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = price_list.objects.get(id=q)
            que.data_of_start = request.POST.get("data_of_start")
            que.cost = request.POST.get("cost")
            que.id_hotel = hotel.objects.get(id=request.POST.get("id_hotel"))
            que.id_tour = tour.objects.get(id=request.POST.get("id_tour"))
            que.save()
            return HttpResponseRedirect("/price_list")

class view_punkt(View):
    def add_punkt(request):
        if request.method == "POST":
            Punkt = punkt()
            Punkt.country_of_punkt = request.POST.get("country_of_punkt")
            Punkt.id_tour = tour.objects.get(id=request.POST.get("id_tour"))
            Punkt.id_price_list = price_list.objects.get(id=request.POST.get("id_tour"))
            Punkt.save()
            return HttpResponseRedirect("/punkt")

    def del_punkt(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = punkt.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/punkt")

    def update_punkt(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = punkt.objects.get(id=q)
            que.country_punkt = request.POST.get("country_of_punkt")
            que.id_tour = tour.objects.get(id=request.POST.get("id_tour"))
            que.id_price_list = price_list.objects.get(id=request.POST.get("id_tour"))
            que.save()
            return HttpResponseRedirect("/punkt")

class view_user(View):
    def add_user(request):
        if request.method == "POST":
            User = user()
            User.login = request.POST.get("login")
            User.password = request.POST.get("password")
            User.save()
            return HttpResponseRedirect("/user")

    def del_user(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = user.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user")

    def update_user(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = user.objects.get(id=q)
            que.login = request.POST.get("login")
            que.password = request.POST.get("password")
            que.save()
            return HttpResponseRedirect("/user")