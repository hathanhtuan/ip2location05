from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class BaseView(LoginRequiredMixin, View):
    view_name = 'Default View Namee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.view_name
        return context
