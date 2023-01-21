from django.views.generic import ListView

from ip2location05app.views.BaseView import BaseView


class HistoryView(BaseView, ListView):

    url_path = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.view_name
        return context

    class Meta:
        abstract = True
