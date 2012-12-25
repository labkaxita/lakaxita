from datetime import date

from milkman.dairy import milkman

from lakaxita.tests.utils import TestCase
from lakaxita.lost_found.models import Item, Notification


class ItemTestCase(TestCase):
    def setUp(self):
        self.jacket = milkman.deliver(Item)
        self.trousers = milkman.deliver(Item)

    def test_recently_lost_first(self):
        self.jacket.lost = date(1, 1, 1)
        self.jacket.save()

        self.trousers.lost = date(1, 1, 2)
        self.trousers.save()

        self.assertQuerysetEqual(Item.objects.all(), [self.trousers, self.jacket])

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

        self.assertQuerysetEqual(Item.objects.not_returned(), [self.jacket])
        self.assertQuerysetEqual(Item.objects.returned(), [self.trousers])

    def tearDown(self):
        self.jacket.delete()
        self.trousers.delete()



class NotificationTestCase(TestCase):
    def setUp(self):
        self.hi = milkman.deliver(Notification)
        self.hello = milkman.deliver(Notification)

    def test_last_ones_first(self):
        self.hi.date = date(1, 1, 1)
        self.hi.save()

        self.hello.date = date(1, 1, 2)
        self.hello.save()

        self.assertQuerysetEqual(Notification.objects.all(), [self.hello, self.hi])

    def tearDown(self):
        self.hi.delete()
        self.hello.delete()
