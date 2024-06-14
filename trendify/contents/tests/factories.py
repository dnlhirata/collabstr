import factory
from creators.tests.factories import CreatorFactory
from factory.django import DjangoModelFactory

from ..models import Content


class ContentFactory(DjangoModelFactory):
    creator = factory.SubFactory(CreatorFactory)
    url = factory.Faker('url')

    class Meta:
        model = Content
