from django.db import models

class tour(models.Model):
    type = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    objects = models.Manager()

class hotel(models.Model):
    name = models.CharField(max_length=45)
    stars = models.CharField(max_length=45)
    objects = models.Manager()

class transport_type(models.Model):
    model = models.CharField(max_length=45)
    number_of_places = models.CharField(max_length=45)
    id_price_list = models.ForeignKey('price_list', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class price_list(models.Model):
    data_of_start = models.CharField(max_length=45)
    cost = models.CharField(max_length=45)
    id_hotel = models.ForeignKey('hotel', on_delete=models.CASCADE, null=True)
    id_tour = models.ForeignKey('tour', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class punkt(models.Model):
    country_of_punkt = models.CharField(max_length=45)
    id_tour = models.ForeignKey('tour', on_delete=models.CASCADE, null=True)
    id_price_list = models.ForeignKey('price_list', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class user(models.Model):
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    objects = models.Manager()