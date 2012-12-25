from datetime import date
from django.test import Client

from milkman.dairy import milkman

from lakaxita.tests.utils import TestCase
from lakaxita.lost_found.models import Item, Notification
from lakaxita.lost_found.forms import NotificationForm


class ItemListTestCase(TestCase):
    def setUp(self):
        self.url = '/lost_found/'
        self.client = Client()
        self.jacket = milkman.deliver(Item, lost=date(1, 1, 1))
        self.trousers = milkman.deliver(Item, lost=date(1, 1, 2))
        self.response = self.client.get(self.url, follow=True)

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'lost_found/item_list.yammy')

    def test_context(self):
        self.assertEqual(self.response.context['item_list'], 
                [self.trousers, self.jacket])

    def tearDown(self):
        self.jacket.delete()
        self.trousers.delete()


class ItemDetailTestCase(TestCase):
    def setUp(self):
        self.jacket = milkman.deliver(Item, name='jacket')
        self.url = '/lost_found/jacket/'
        self.client = Client()
        self.response = self.client.get(self.url, follow=True)

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'lost_found/item_detail.yammy')

    def test_context(self):
        self.assertEqual(self.response.context['item'], self.jacket)
        self.assertIsInstance(self.response.context['form'], NotificationForm)

    def tearDown(self):
        self.jacket.delete()


class CreateNotificationTestCase(TestCase):
    def setUp(self):
        self.jacket = milkman.deliver(Item, name='jacket')
        self.url = '/eu/lost_found/jacket/notify/'
        self.client = Client()
        self.response = self.client.get(self.url, follow=True)

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'lost_found/notify.yammy')

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
        post_response = self.client.post(self.url, data=data, follow=True)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.content, '')
        notifications = Notification.objects.filter(
                title='mine', item=self.jacket)
        self.assertEqual(notifications.count(), 1)
        self.assertEqual(notifications[0].date, date.today())

    def test_incorrect_post(self):
        data = {
                'title': 'mine',
                'reply_to': 'NO CORRECT EMAIL',
                'text': 'how are you?',
                'date': '0001-01-01',
                }
        post_response = self.client.post(self.url, data=data, follow=True)
        self.assertEqual(post_response.status_code, 200)
        self.assertNotEqual(post_response.content, '')

    def tearDown(self):
        self.jacket.delete()
