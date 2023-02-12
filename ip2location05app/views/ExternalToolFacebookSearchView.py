from ip2location05app.forms.ExternalToolFacebookSearchForm import ExternalToolFacebookSearchForm
from ip2location05app.views.ExternalToolView import ExternalToolView


class ExternalToolFacebookSearchView(ExternalToolView):
    template_name = 'external_tool_facebook_search.html'
    form_class = ExternalToolFacebookSearchForm
    view_name = 'Public Facebook Search'

    def get_tool_type(self):
        return 'external_facebook'
