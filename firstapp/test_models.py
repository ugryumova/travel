from django.test import TestCase
import unittest
from firstapp.models import tour, hotel, transport_type, price_list, punkt, user

class tourModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        tour.objects.create(type='type', duration='duration')

    def test_type_label(self):
        Tour = tour.objects.get(id=1)
        field_label = Tour._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type')

    def test_duration_label(self):
        Tour = tour.objects.get(id=1)
        field_label = Tour._meta.get_field('duration').verbose_name
        self.assertEquals(field_label, 'duration')

    def test_type_max_length(self):
        Tour = tour.objects.get(id=1)
        max_length = Tour._meta.get_field('type').max_length
        self.assertEquals(max_length, 45)

    def test_duration_max_length(self):
        Tour = tour.objects.get(id=1)
        max_length = Tour._meta.get_field('type').max_length
        self.assertEquals(max_length, 45)

class hotelModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        hotel.objects.create(name='name', stars='5')

    def test_name_label(self):
        Hotel = hotel.objects.get(id=1)
        field_label = Hotel._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_stars_label(self):
        Hotel = hotel.objects.get(id=1)
        field_label = Hotel._meta.get_field('stars').verbose_name
        self.assertEquals(field_label,'stars')

    def test_name_max_length(self):
        Hotel = hotel.objects.get(id=1)
        max_length = Hotel._meta.get_field('name').max_length
        self.assertEquals(max_length, 45)

    def test_stars_max_length(self):
        Hotel = hotel.objects.get(id=1)
        max_length = Hotel._meta.get_field('stars').max_length
        self.assertEquals(max_length, 45)

class transport_typeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        transport_type.objects.create(model='model', number_of_places='50')

    def test_model_label(self):
        Transport_type = transport_type.objects.get(id=1)
        field_label = Transport_type._meta.get_field('model').verbose_name
        self.assertEquals(field_label, 'model')

    def test_number_of_places_label(self):
        Transport_type = transport_type.objects.get(id=1)
        field_label = Transport_type._meta.get_field('number_of_places').verbose_name
        self.assertEquals(field_label, 'number of places')

    def test_model_max_length(self):
        Transport_type = transport_type.objects.get(id=1)
        max_length = Transport_type._meta.get_field('model').max_length
        self.assertEquals(max_length, 45)

    def test_number_of_places_max_length(self):
        Transport_type = transport_type.objects.get(id=1)
        max_length = Transport_type._meta.get_field('number_of_places').max_length
        self.assertEquals(max_length, 45)

class price_listModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        price_list.objects.create(data_of_start='10/05/2018', cost='1000')

    def test_data_of_start_label(self):
        Price_list = price_list.objects.get(id=1)
        field_label = Price_list._meta.get_field('data_of_start').verbose_name
        self.assertEquals(field_label, 'data of start')

    def test_cost_label(self):
        Price_list = price_list.objects.get(id=1)
        field_label = Price_list._meta.get_field('cost').verbose_name
        self.assertEquals(field_label, 'cost')

    def test_data_of_start_max_length(self):
        Price_list = price_list.objects.get(id=1)
        max_length = Price_list._meta.get_field('data_of_start').max_length
        self.assertEquals(max_length, 45)

    def test_cost_max_length(self):
        Price_list = price_list.objects.get(id=1)
        max_length = Price_list._meta.get_field('cost').max_length
        self.assertEquals(max_length, 45)

class punktModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        punkt.objects.create(country_of_punkt='Russia')

    def test_country_of_punkt_label(self):
        Punkt = punkt.objects.get(id=1)
        field_label = Punkt._meta.get_field('country_of_punkt').verbose_name
        self.assertEquals(field_label, 'country of punkt')

    def test_country_of_punkt_max_length(self):
        Punkt = punkt.objects.get(id=1)
        max_length = Punkt._meta.get_field('country_of_punkt').max_length
        self.assertEquals(max_length, 45)

class userModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user.objects.create(login='login', password='password')

    def test_login_label(self):
        User = user.objects.get(id=1)
        field_label = User._meta.get_field('login').verbose_name
        self.assertEquals(field_label, 'login')

    def test_password_label(self):
        User = user.objects.get(id=1)
        field_label = User._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_login_max_length(self):
        User = user.objects.get(id=1)
        max_length = User._meta.get_field('login').max_length
        self.assertEquals(max_length, 45)

    def test_password_max_length(self):
        User = user.objects.get(id=1)
        max_length = User._meta.get_field('password').max_length
        self.assertEquals(max_length, 45)