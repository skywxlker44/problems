from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
    path('starships/<int:pk>/', views.starship_detail, name='starship_detail'),
]
