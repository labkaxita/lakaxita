import json
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


from lakaxita.lost_found.models import Item
from lakaxita.lost_found.forms import NotificationForm


class ItemList(ListView):
    model = Item
    allow_empty = True
    paginate_by = 10
    template_name = 'lost_found/item_list.yammy'
    context_object_name = 'item_list'


class ItemDetail(DetailView):
    model = Item
    template_name = 'lost_found/item_detail.yammy'

    def get_context_data(self, *args, **kwargs):
        context = super(ItemDetail, self).get_context_data(*args, **kwargs)
        context['form'] = NotificationForm()
        return context


class CreateNotification(CreateView):
    template_name = 'lost_found/notify.yammy'
    form_class = NotificationForm

    def get_object(self):
        return get_object_or_404(Item, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CreateNotification, self).get_context_data(**kwargs)
        context['item'] = self.get_object()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.item = self.get_object()
        self.object.save()
        return HttpResponse()
