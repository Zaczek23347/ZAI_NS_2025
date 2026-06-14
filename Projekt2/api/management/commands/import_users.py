from django.core.management.base import BaseCommand
from api.models import Person
import requests


class Command(BaseCommand):
    help = "Import users from public API"

    def handle(self, *args, **kwargs):
        url = "https://jsonplaceholder.typicode.com/users"

        response = requests.get(url)
        users = response.json()

        for user in users:
            Person.objects.get_or_create(
                email=user["email"],
                defaults={
                    "name": user["name"]
                }
            )

        self.stdout.write(
            self.style.SUCCESS("Users imported successfully")
        )