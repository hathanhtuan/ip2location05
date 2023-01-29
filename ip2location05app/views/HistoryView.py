from django.views.generic import ListView

from ip2location05app.views.BaseView import BaseView


class HistoryView(BaseView, ListView):
    url_path = None
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.view_name
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get("per_page", self.paginate_by)

    class Meta:
        abstract = True
