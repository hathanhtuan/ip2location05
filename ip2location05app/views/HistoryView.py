from django.views.generic import ListView

from ip2location05app.views.BaseView import BaseView


class HistoryView(BaseView, ListView):

    class Meta:
        abstract = True
