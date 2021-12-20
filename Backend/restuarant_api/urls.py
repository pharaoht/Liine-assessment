from django import urls
from django.urls import path
from . import views

app_name = 'restuarant_api'

urlpatterns = [
    path('get-restaurants-opened/', views.get_restaurants, name='list'),
    path('add-hours/', views.add_hours, name='add')
]
