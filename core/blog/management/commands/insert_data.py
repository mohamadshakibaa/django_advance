from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post, Category


class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.faker = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.faker.email(), password="m@123456")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.faker.first_name()
        profile.last_name = self.faker.last_name()
        profile.description = self.faker.paragraph()
        profile.save()
        