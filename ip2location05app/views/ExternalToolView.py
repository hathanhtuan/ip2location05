from django.views.generic import FormView

from ip2location05app.forms.ExternalToolForm import ExternalToolForm
from ip2location05app.models.ApiConfiguration import ApiConfiguration
from ip2location05app.views.PublicView import PublicView


class ExternalToolView(PublicView, FormView):
    template_name = 'external_tool.html'
    form_class = ExternalToolForm

    def get_tool_type(self):
        if 'type' in self.request.GET:
            return self.request.GET['type']
        else:
            return None

    def get_form(self, *args, **kwargs):
        tool_type = self.get_tool_type()
        form = super().get_form(*args, **kwargs)
        form.fields['api_configuration'].queryset = ApiConfiguration.objects.filter(
            api_config_type=tool_type
        )
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_tool_type():
            context['choices'] = ApiConfiguration.objects.filter(
                api_config_type=self.get_tool_type()
            )
        else:
            context['choices'] = ApiConfiguration.objects.none()
        return context


