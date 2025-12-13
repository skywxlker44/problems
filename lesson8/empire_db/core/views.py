from django.shortcuts import render, get_object_or_404
from .models import Character, Starship


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'core/character_list.html', {'characters': characters})


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'core/character_detail.html', {'character': character})


def starship_detail(request, pk):
    starship = get_object_or_404(Starship, pk=pk)
    return render(request, 'core/starship_detail.html', {'starship': starship})
