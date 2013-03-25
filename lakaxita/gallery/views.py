from django.views.generic import ListView, DetailView

from lakaxita.gallery.models import Category


class CategoryList(ListView):
    model = Category
    allow_empty = True
    paginate_by = 10
    template_name = 'gallery/category_list.yammy'
    context_object_name = 'category_list'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'gallery/category_detail.yammy'
