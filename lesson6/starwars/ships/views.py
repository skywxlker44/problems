from django.shortcuts import render
import requests


def ship(request, ship_id):
    url = f"https://swapi.dev/api/starships/{ship_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        ship = response.json()
    else:
        ship = {"name": "Unknown ship"}
    return render(request, "ships/ship.html", {"ship": ship})


def home(request):
    return render(request, "ships/home.html")
