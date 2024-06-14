from contents.tests.factories import ContentFactory
from creators.models import Creator
from django.test import RequestFactory, TestCase

from ..views import IndexView


class IndexViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        request = RequestFactory().get('/')
        cls.view = IndexView()
        cls.view.setup(request)

        cls.instagram = ContentFactory(creator__platform=Creator.Platform.INSTAGRAM)
        cls.tiktok = ContentFactory(creator__platform=Creator.Platform.TIKTOK)
        cls.usergen = ContentFactory(creator__platform=Creator.Platform.USER_GENERATED)

    def test_get_queryset(self):
        with self.subTest('no platform selected'):
            self.view.platform = None
            qs = self.view.get_queryset()

            self.assertEqual(qs.count(), 3)
            self.assertIn(self.instagram, qs)
            self.assertIn(self.tiktok, qs)
            self.assertIn(self.usergen, qs)

        with self.subTest('instagram selected'):
            self.view.platform = Creator.Platform.INSTAGRAM
            qs = self.view.get_queryset()

            self.assertEqual(qs.count(), 1)
            self.assertEqual(qs[0], self.instagram)

        with self.subTest('tiktok selected'):
            self.view.platform = Creator.Platform.TIKTOK
            qs = self.view.get_queryset()

            self.assertEqual(qs.count(), 1)
            self.assertEqual(qs[0], self.tiktok)

        with self.subTest('usergen selected'):
            self.view.platform = Creator.Platform.USER_GENERATED
            qs = self.view.get_queryset()

            self.assertEqual(qs.count(), 1)
            self.assertEqual(qs[0], self.usergen)

    def test_get_template_names(self):
        self.view.object_list = None
        with self.subTest('no platform selected'):
            self.view.platform = None
            templates = self.view.get_template_names()

            self.assertEqual(templates, ['home/index.html'])

        with self.subTest('platform selected'):
            self.view.platform = Creator.Platform.INSTAGRAM
            templates = self.view.get_template_names()

            self.assertEqual(templates, ['home/content_list.html'])
