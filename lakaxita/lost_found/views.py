from django.views.generic import ListView, DetailView, CreateView

from infinite_pagination import InfinitePaginator

from lakaxita.lost_found.models import Item
from lakaxita.lost_found.forms import NotificationForm


class ItemList(ListView):
    model = Item
    allow_empty = True
    paginate_by = 10
    paginator_class = InfinitePaginator
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
    form_class = NotificationForm

    def form_valid(self, form):
        return super(CreateNotification, self).form_valid(form)

    def form_invalid(self, form):
        return super(CreateNotification, self).form_invalid(form)
