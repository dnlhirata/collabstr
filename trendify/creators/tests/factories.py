import factory
from factory.django import DjangoModelFactory

from ..models import Creator


class CreatorFactory(DjangoModelFactory):
    name = factory.Faker('name')
    username = factory.Faker('user_name')
    rating = factory.Faker('random_int', min=1, max=5)
    platform = factory.Faker(
        'random_element',
        elements=['YouTube', 'Twitch', 'Instagram', 'Twitter']
    )

    class Meta:
        model = Creator
