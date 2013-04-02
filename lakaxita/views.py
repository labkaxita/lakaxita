from os import path

from django.views.generic import TemplateView
from django.template.base import TemplateDoesNotExist
from django.http import Http404


class BaseView(TemplateView):
    template_name = 'base.yammy'


class JSTemplateView(TemplateView):
    def get_template_names(self):
        p = path.join('js', self.kwargs['path'])
        return [ '{path}.{ext}'.format(path=p, ext=ext) for ext in\
                ('yammy', 'html') ]

    def render_to_response(self, context, **response_kwargs):
        response = super(JSTemplateView, self).render_to_response(
                context, **response_kwargs)
        try:
            response.resolve_template(response.template_name)
        except TemplateDoesNotExist:
            raise Http404
        else:
            return response
