from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


from lakaxita.groups.models import Group
from lakaxita.news.models import News


class NewsList(ListView):
    queryset = News.objects.published()
    allow_empty = True
    paginate_by = 10
    template_name = 'news/news_list.yammy'
    context_object_name = 'news_list'


class NewsGroupDetail(ListView):
    allow_empty = True
    paginate_by = 10
    template_name = 'news/news_list.yammy'
    context_object_name = 'news_list'

    def get_group(self):
        return get_object_or_404(Group, self.kwargs['slug'])

    def get_queryset(self):
        return News.objects.published().filter(group=self.get_group())

    def get_context_data(self, *args, **kwargs):
        context = super(NewsGroupDetail, self).get_context_data(
                *args, **kwargs)
        context['group'] = self.get_group()
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.yammy'
