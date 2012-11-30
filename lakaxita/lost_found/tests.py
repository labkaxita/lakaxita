from datetime import date
from django.utils import unittest
from django.test import Client

from milkman.dairy import milkman

from lakaxita.lost_found.models import Item, Notification


class ItemTestCase(unittest.TestCase):
    def setUp(self):
        self.jacket = milkman.deliver(Item)
        self.trousers = milkman.deliver(Item)

    def test_recently_lost_first(self):
        self.jacket.lost = date(1, 1, 1)
        self.jacket.save()

        self.trousers.lost = date(1, 1, 2)
        self.trousers.save()

        self.assertEqual(list(Item.objects.all()), [self.trousers, self.jacket])

    def test_has_been_returned(self):
        self.jacket.found = None
        self.assertEqual(self.jacket.has_been_returned, False)

        self.jacket.found = date(1, 1, 1)
        self.assertEqual(self.jacket.has_been_returned, True)

    def test_manager(self):
        self.jacket.found = None
        self.jacket.save()

        self.trousers.found = date(1, 1, 1)
        self.trousers.save()

        self.assertEqual(list(Item.objects.not_returned()), [self.jacket])
        self.assertEqual(list(Item.objects.returned()), [self.trousers])

    def tearDown(self):
        self.jacket.delete()
        self.trousers.delete()



class NotificationTestCase(unittest.TestCase):
    def setUp(self):
        self.hi = milkman.deliver(Notification)
        self.hello = milkman.deliver(Notification)

    def test_last_ones_first(self):
        self.hi.date = date(1, 1, 1)
        self.hi.save()

        self.hello.date = date(1, 1, 2)
        self.hello.save()

        self.assertEqual(
                list(Notification.objects.all()), 
                [self.hello, self.hi]
                )

    def tearDown(self):
        self.hi.delete()
        self.hello.delete()


class ItemListTestCase(unittest.TestCase):
    def setUp(self):
        self.url = '/lost_found/'
        self.client = Client()
        self.jacket = milkman.deliver(Item, lost=date(1, 1, 1))
        self.trousers = milkman.deliver(Item, lost=date(1, 1, 2))
        self.response = self.client.get(self.url)

    def test_status(self):
        self.response.status_code == '200'

    def test_template(self):
        self.assertEqual(self.response.template[0].name, 
                'lost_found/item_list.yammy')

    def test_context(self):
        self.assertEqual(self.response.context['item_list'], 
                [self.trousers, self.jacket])

    def tearDown(self):
        self.jacket.delete()
        self.trousers.delete()
