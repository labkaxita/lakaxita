from django.views.generic import ListView, DetailView

from infinite_pagination import InfinitePaginator

from lakaxita.group.models import Group


class GroupList(ListView):
    model = Group
    allow_empty = True
    paginate_by = 10
    paginator_class = InfinitePaginator
    template_name = 'groups/group_list.yammy'
    context_object_name = 'group_list'


class GroupDetail(DetailView):
    model = Group
    template_name = 'groups/group_detail.yammy'
