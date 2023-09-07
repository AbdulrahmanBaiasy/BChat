from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('add/', views.room_add, name='room_add'),
    path('<slug:slug>/', views.room, name='room'),

]