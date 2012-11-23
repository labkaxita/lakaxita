from django.views.generic import ListView, DetailView

from infinite_pagination import InfinitePaginator

from lakaxita.lost_found.models import Item


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
