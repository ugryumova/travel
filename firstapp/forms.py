from django import forms

class Addtour(forms.Form):
    type = forms.CharField(label="Тип тура", widget=forms.TextInput(attrs={"class": "myfield"}))
    duration = forms.CharField(label="Продолжительность", widget=forms.TextInput(attrs={"class": "myfield"}))

class Addhotel(forms.Form):
    name = forms.CharField(label="Название",widget=forms.TextInput(attrs={"class":"myfield"}))
    stars = forms.CharField(label="Количество звездочек",widget=forms.TextInput(attrs={"class":"myfield"}))

class Addtransport_type(forms.Form):
    model = forms.CharField(label="Модель",widget=forms.TextInput(attrs={"class":"myfield"}))
    number_of_places = forms.CharField(label="Число мест", widget=forms.TextInput(attrs={"class":"myfield"}))
    id_price_list = forms.CharField(label="ID прайс-листа", widget=forms.TextInput(attrs={"class":"myfield"}))

class Addprice_list(forms.Form):
    data_of_start = forms.CharField(label="Дата начала", widget=forms.TextInput(attrs={"class":"myfield"}))
    cost = forms.CharField(label="Стоимость", widget=forms.TextInput(attrs={"class": "myfield"}))
    id_hotel = forms.CharField(label="ID отеля", widget=forms.TextInput(attrs={"class": "myfield"}))
    id_tour = forms.CharField(label="ID тура", widget=forms.TextInput(attrs={"class":"myfield"}))

class Addpunkt(forms.Form):
    country_of_punkt = forms.CharField(label="Страна пункта расположения",widget=forms.TextInput(attrs={"class":"myfield"}))
    id_tour = forms.CharField(label="ID тура", widget=forms.TextInput(attrs={"class": "myfield"}))
    id_price_list = forms.CharField(label="ID прайс-листа", widget=forms.TextInput(attrs={"class": "myfield"}))

class Adduser(forms.Form):
    login = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "myfield"}))
    password = forms.CharField(label="Пароль", widget=forms.TextInput(attrs={"class": "myfield"}))