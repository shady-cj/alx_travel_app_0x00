from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth import get_user_model
from alx_travel_app.listings.models import Listing, Booking, Review
User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        seeder.add_entity(User, 5)
        seeder.add_entity(Listing, 10)
        seeder.add_entity(Booking, 10)
        seeder.add_entity(Review, 10)
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))