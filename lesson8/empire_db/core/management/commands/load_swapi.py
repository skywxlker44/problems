import requests
from django.core.management.base import BaseCommand
from core.models import Character, Starship

class Command(BaseCommand):
    help = 'Загружает персонажей и корабли из SWAPI с заполнением всех полей'

    def handle(self, *args, **kwargs):
        self.load_starships()
        self.load_characters()

    def load_starships(self):
        url = 'https://swapi.dev/api/starships/'
        while url:
            resp = requests.get(url).json()
            for ship in resp['results']:
                Starship.objects.update_or_create(
                    name=ship.get('name', 'unknown'),
                    defaults={
                        'model': ship.get('model') or 'unknown',
                        'manufacturer': ship.get('manufacturer') or 'unknown',
                        'cost_in_credits': ship.get('cost_in_credits') or 'unknown',
                        'length': ship.get('length') or 'unknown',
                        'crew': ship.get('crew') or 'unknown',
                        'passengers': ship.get('passengers') or 'unknown',
                        'max_atmosphering_speed': ship.get('max_atmosphering_speed') or 'unknown',
                        'cargo_capacity': ship.get('cargo_capacity') or 'unknown'
                    }
                )
            url = resp.get('next')
        self.stdout.write(self.style.SUCCESS('Starships loaded'))

    def load_characters(self):
        url = 'https://swapi.dev/api/people/'
        while url:
            resp = requests.get(url).json()
            for p in resp['results']:
                char, _ = Character.objects.update_or_create(
                    name=p.get('name', 'unknown'),
                    defaults={
                        'height': p.get('height') or 'unknown',
                        'mass': p.get('mass') or 'unknown',
                        'hair_color': p.get('hair_color') or 'unknown',
                        'skin_color': p.get('skin_color') or 'unknown',
                        'eye_color': p.get('eye_color') or 'unknown',
                        'birth_year': p.get('birth_year') or 'unknown',
                        'gender': p.get('gender') or 'unknown'
                    }
                )

                # Привязываем корабли к персонажу
                for ship_url in p.get('starships', []):
                    ship_resp = requests.get(ship_url).json()
                    ship_obj, _ = Starship.objects.update_or_create(
                        name=ship_resp.get('name', 'unknown'),
                        defaults={
                            'model': ship_resp.get('model') or 'unknown',
                            'manufacturer': ship_resp.get('manufacturer') or 'unknown',
                            'cost_in_credits': ship_resp.get('cost_in_credits') or 'unknown',
                            'length': ship_resp.get('length') or 'unknown',
                            'crew': ship_resp.get('crew') or 'unknown',
                            'passengers': ship_resp.get('passengers') or 'unknown',
                            'max_atmosphering_speed': ship_resp.get('max_atmosphering_speed') or 'unknown',
                            'cargo_capacity': ship_resp.get('cargo_capacity') or 'unknown'
                        }
                    )
                    char.starships.add(ship_obj)

            url = resp.get('next')

        self.stdout.write(self.style.SUCCESS('Characters loaded'))
