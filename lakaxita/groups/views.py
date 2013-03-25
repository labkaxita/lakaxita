from django.views.generic import ListView, DetailView

from lakaxita.groups.models import Group


class GroupList(ListView):
    model = Group
    allow_empty = True
    paginate_by = 10
    template_name = 'groups/group_list.yammy'
    context_object_name = 'group_list'


class GroupDetail(DetailView):
    model = Group
    template_name = 'groups/group_detail.yammy'
