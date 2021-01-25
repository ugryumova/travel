
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.autodiscover()

urlpatterns = [
    path('', views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('travel/', views.index, name='home'),
    path('tour/', views.index_tour, name='tour'),
    path('punkt/', views.index_punkt, name='punkt'),
    path('price_list/', views.index_price_list, name='price_list'),
    path('transport_type/', views.index_transport_type, name='transport_type'),
    path('user/', views.index_user, name='user'),
    path('hotel/', views.index_hotel, name='hotel'),

    path("tour/add/", views.view_tour.add_tour, name="add_tour"),
    path("tour/del/", views.view_tour.del_tour, name="del_tour"),
    path("tour/up/", views.view_tour.update_tour, name="update_tour"),

    path("punkt/add/", views.view_punkt.add_punkt, name="add_punkt"),
    path("punkt/del/", views.view_punkt.del_punkt, name="del_punkt"),
    path("punkt/up/", views.view_punkt.update_punkt, name="update_punkt"),

    path("price_list/add/", views.view_price_list.add_price_list, name="add_price_list"),
    path("price_list/del/", views.view_price_list.del_price_list, name="del_price_list"),
    path("price_list/up/", views.view_price_list.update_price_list, name="update_price_list"),

    path("transport_type/add/", views.view_transport_type.add_transport_type, name="add_transport_type"),
    path("transport_type/del/", views.view_transport_type.del_transport_type, name="del_transport_type"),
    path("transport_type/up/", views.view_transport_type.update_transport_type, name="update_transport_type"),

    path("user/add/", views.view_user.add_user, name="add_user"),
    path("user/del/", views.view_user.del_user, name="del_user"),
    path("user/up/", views.view_user.update_user, name="update_user"),

    path("hotel/add/", views.view_hotel.add_hotel, name="add_hotel"),
    path("hotel/del/", views.view_hotel.del_hotel, name="del_hotel"),
    path("hotel/up/", views.view_hotel.update_hotel, name="update_hotel"),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
