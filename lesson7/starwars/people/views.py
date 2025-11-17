from django.shortcuts import render
import requests


def person(request, person_id):
    url = f"https://swapi.dev/api/people/{person_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        person = response.json()
    else:
        person = {"name": "Unknown character"}
    return render(request, "people/person.html", {"person": person})


def home(request):
    return render(request, "people/home.html")
