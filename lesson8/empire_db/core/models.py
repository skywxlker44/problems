from django.db import models

class Starship(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100, blank=True)
    manufacturer = models.CharField(max_length=200, blank=True)
    cost_in_credits = models.CharField(max_length=50, blank=True)
    length = models.CharField(max_length=50, blank=True)
    crew = models.CharField(max_length=50, blank=True)
    passengers = models.CharField(max_length=50, blank=True)
    max_atmosphering_speed = models.CharField(max_length=50, blank=True)
    cargo_capacity = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True)
    mass = models.CharField(max_length=20, blank=True)
    hair_color = models.CharField(max_length=50, blank=True)
    skin_color = models.CharField(max_length=50, blank=True)
    eye_color = models.CharField(max_length=50, blank=True)
    birth_year = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)

    starships = models.ManyToManyField(Starship, blank=True)

    def __str__(self):
        return self.name
