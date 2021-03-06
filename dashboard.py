"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'peterklepec.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'peterklepec.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for peterklepec.
    """
    columns = 1

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('NAZAJ NA STRAN'), '/'],
                [_('Urejevalnik besedil'), 'http://ckeditor.com/demo#full'],
                [_('Spremeni geslo'),
                 reverse('%s:password_change' % site_name)],
                [_('Odjava'), reverse('%s:logout' % site_name)],

            ]
        ))
        self.children.append(modules.Group(
            title="UREJANJE SPLETNE STRANI",
            display="tabs",
            children=[
                modules.ModelList(
                    title='PONUDBE',
                    models=('webpage.models.Exercises',)
                ),
                modules.ModelList(
                    title='CENIK',
                    models=('webpage.models.Prices', 'webpage.models.PricingPlan')
                ),
                modules.ModelList(
                    title='URNIK',
                    models=('webpage.models.ExercisesWeeklyTimetable', 'webpage.models.NotWorkingHours')
                ),
                modules.ModelList(
                    title='NOVICE',
                    models=('webpage.models.News', 'webpage.models.CustomPage')
                ),
                modules.ModelList(
                    title='SLIKE',
                    models=('webpage.models.Images', )
                ),
                modules.ModelList(
                    title='POMEMBNA OBVESTILA',
                    models=('webpage.models.InfoBar', )
                ),

            ]
        ))


        # append an app list module for "Administration"
        """
        self.children.append(modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
        ))
        """
        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))



        # append another link list module for "support".



class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for peterklepec.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
