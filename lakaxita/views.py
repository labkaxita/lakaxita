from django.views.generic import TemplateView

from lakaxita.news.models import News
from lakaxita.gallery.models import Category


class BaseView(TemplateView):
    template_name = 'home.yammy'

    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(*args, **kwargs)
        context['news_list'] = News.objects.frontpage()
        context['category_list'] = Category.objects.root_nodes()
        return context
