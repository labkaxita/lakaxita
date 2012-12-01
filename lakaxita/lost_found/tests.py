from datetime import date
from django.utils import unittest
from django.test import Client

from milkman.dairy import milkman

from lakaxita.lost_found.models import Item, Notification
from lakaxita.lost_found.forms import NotificationForm


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
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertEqual(self.response.template[0].name, 
                'lost_found/item_list.yammy')

    def test_context(self):
        self.assertEqual(self.response.context['item_list'], 
                [self.trousers, self.jacket])

    def tearDown(self):
        self.jacket.delete()
        self.trousers.delete()


class ItemDetailTestCase(unittest.TestCase):
    def setUp(self):
        self.jacket = milkman.deliver(Item, name='jacket')
        self.url = '/lost_found/jacket/'
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertEqual(self.response.template[0].name, 
                'lost_found/item_detail.yammy')

    def test_context(self):
        self.assertEqual(self.response.context['item'], self.jacket)
        self.assertIsInstance(self.response.context['form'], NotificationForm)

    def tearDown(self):
        self.jacket.delete()


class CreateNotificationTestCase(unittest.TestCase):
    def setUp(self):
        self.jacket = milkman.deliver(Item, name='jacket')
        self.url = '/lost_found/jacket/notify/'
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertEqual(self.response.template.name,
                'lost_found/notify.yammy')

    def test_context(self):
        self.assertEqual(self.response.context['item'], self.jacket)
        self.assertIsInstance(self.response.context['form'], NotificationForm)

    def test_correct_post(self):
        data = {
                'title': 'mine',
                'reply_to': 'test@mail.com',
                'text': 'how are you?',
                'date': '0001-01-01',
                }
        post_response = self.client.post(self.url, data=data)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.content, '')
        self.assertEqual(Notification.objects.filter(
            title='mine', item=self.jacket).count(), 1)

    def test_incorrect_post(self):
        data = {
                'title': 'mine',
                'reply_to': 'NO CORRECT EMAIL',
                'text': 'how are you?',
                'date': '0001-01-01',
                }
        post_response = self.client.post(self.url, data=data)
        self.assertEqual(post_response.status_code, 200)
        self.assertNotEqual(post_response.content, '')

    def tearDown(self):
        self.jacket.delete()
