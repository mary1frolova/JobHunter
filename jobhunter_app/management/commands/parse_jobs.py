import requests
from django.core.management.base import BaseCommand
from jobhunter_app.models import Job

class Command(BaseCommand):
    help = 'Parse jobs from hh.ru'

    def handle(self, *args, **kwargs):
        response = requests.get('https://api.hh.ru/vacancies')
        vacancies = response.json()['items']

        for vacancy in vacancies:
            Job.objects.create(
                title=vacancy['name'],
                description=vacancy['snippet']['responsibility'],
                company=vacancy['employer']['name'],
                url=vacancy['alternate_url']
            )

        self.stdout.write(self.style.SUCCESS('Successfully parsed jobs'))
