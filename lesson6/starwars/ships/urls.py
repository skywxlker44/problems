from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ship/<int:ship_id>/', views.ship, name='ship'),
]
