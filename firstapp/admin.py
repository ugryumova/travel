from django.contrib import admin
from .models import tour, hotel, transport_type, price_list, punkt, user

@admin.register(tour)
class tourAdmin(admin.ModelAdmin):
    list_display = ('type', 'duration')

@admin.register(hotel)
class hotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars')

@admin.register(transport_type)
class transport_typeAdmin(admin.ModelAdmin):
    list_display = ('model', 'number_of_places', 'id_price_list')

@admin.register(price_list)
class price_listAdmin(admin.ModelAdmin):
    list_display = ('data_of_start', 'cost', 'id_hotel', 'id_tour')

@admin.register(punkt)
class punktAdmin(admin.ModelAdmin):
    list_display = ('country_of_punkt', 'id_price_list', 'id_tour')

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('login', 'password')
