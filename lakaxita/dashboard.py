from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class Dashboard(Dashboard):
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.ModelList(
            _('News'),
            column=1,
            collapsible=True,
            models=('lakaxita.news.*',),
        ))

        self.children.append(modules.ModelList(
            _('Gallery'),
            column=1,
            collapsible=True,
            models=('lakaxita.gallery.*',),
        )),

        self.children.append(modules.ModelList(
            _('Lost and Found'),
            column=1,
            collapsible=True,
            models=('lakaxita.lost_found.*',),
        ))


        self.children.append(modules.ModelList(
            _('Others'),
            column=1,
            collapsible=True,
            models=('oembed.*', 'lakaxita.groups.*', 'preferences.*'),
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
            models=('django.contrib.*',),
        ))
        
        self.children.append(modules.LinkList(
            _('Multimedia'), 
            layout='inline',
            column=2,
            children=(
                [_('Internal Attachments'), 
                    reverse('filebrowser:fb_browse'),
                    False],
                [_('External Attachments'), 
                    reverse('admin:attachments_externalattachment_changelist'),
                    False],
                ),
        ))

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


