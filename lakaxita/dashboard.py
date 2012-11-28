from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class Dashboard(Dashboard):
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.ModelList(
            _('Articles'),
            column=1,
            collapsible=True,
            models=('project.articles.*',),
        ))

        self.children.append(modules.ModelList(
            _('Lost and Found'),
            column=1,
            collapsible=True,
            models=('lakaxita.lost_found.*',),
        ))

        self.children.append(modules.ModelList(
            _('Attachments'),
            column=1,
            collapsible=True,
            models=('lakaxita.attachments.*',),
        ))

        self.children.append(modules.ModelList(
            _('Feeds'),
            column=1,
            collapsible=True,
            models=('project.feeds.*',),
        ))

        self.children.append(modules.ModelList(
            _('Others'),
            column=1,
            collapsible=True,
            models=('oembed.*', 'feedback.*', 'lakaxita.groups.*'),
        ))

#       # append an app list module for "Applications"
#       self.children.append(modules.AppList(
#           _('AppList: Applications'),
#           collapsible=True,
#           column=1,
#           css_classes=('collapse closed',),
#           exclude=('django.contrib.*',),
#       ))
        
        self.children.append(modules.ModelList(
            _('Administration'),
            column=1,
            collapsible=True,
            models=('django.contrib.*', 'monkey_team.*'),
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('Contact the developer'),
                    'url': 'mailto:unai@gisa-elkartea.org',
                    'external': True,
                },
            ]
        ))
        
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


