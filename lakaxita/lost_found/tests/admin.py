from datetime import date
from django.http import HttpRequest, QueryDict
from django.contrib.admin import site

from milkman.dairy import milkman

from lakaxita.tests.utils import TestCase
from lakaxita.lost_found.models import Item, Notification
from lakaxita.lost_found.forms import NotificationForm
from lakaxita.lost_found.admin import (
                                        NotificationInline, 
                                        ReturnedItemFilter, 
                                        ItemAdmin,
                                        )

class AdminTestCase(TestCase):
    def setUp(self):
        self.jacket = milkman.deliver(Item)
        self.trousers = milkman.deliver(Item)
        self.item_admin = ItemAdmin(Item, site)
        self.notification_inline = NotificationInline(self.item_admin, site)

    def test_no_inline_add_permission(self):
        self.assertFalse(self.notification_inline.has_add_permission(
            HttpRequest()
            ))

    def test_returned_item_filter(self):
        self.jacket.found = date(1, 1, 1)
        self.jacket.save()

        self.trousers.found = None
        self.trousers.save()

        request = HttpRequest()

        returned_filter = ReturnedItemFilter(
                request,
                params={'returned': 'returned'},
                model=Item,
                model_admin=ItemAdmin,
                )
        
        self.assertQuerysetEqual(
                returned_filter.queryset(request, Item.objects.all()),
                [self.jacket],
                )

    def test_not_returned_item_filter(self):
        self.jacket.found = date(1, 1, 1)
        self.jacket.save()

        self.trousers.found = None
        self.trousers.save()

        request = HttpRequest()

        returned_filter = ReturnedItemFilter(
                request,
                params={'returned': 'not_returned'},
                model=Item,
                model_admin=ItemAdmin,
                )
        
        self.assertQuerysetEqual(
                returned_filter.queryset(request, Item.objects.all()),
                [self.trousers],
                )

    def test_has_been_returned(self):
        self.trousers.found = date(1, 1, 1)
        self.trousers.save()

        self.assertTrue(self.item_admin.has_been_returned(self.trousers))

        self.trousers.found = None
        self.trousers.save()

        self.assertFalse(self.item_admin.has_been_returned(self.trousers))


    def test_mark_returned(self):
        self.item_admin.mark_returned(HttpRequest(), Item.objects.all())
        jacket, trousers = Item.objects.all()
        self.assertTrue(jacket.has_been_returned)
        self.assertTrue(trousers.has_been_returned)

    def test_mark_not_returned(self):
        self.item_admin.mark_not_returned(HttpRequest(), Item.objects.all())
        jacket, trousers = Item.objects.all()
        self.assertFalse(jacket.has_been_returned)
        self.assertFalse(trousers.has_been_returned)

    def tearDown(self):
        self.jacket.delete()
        self.trousers.delete()
