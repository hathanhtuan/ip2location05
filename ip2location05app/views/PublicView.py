import logging

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class PublicView(TemplateView):
    view_name = 'Public'
    template_name = 'base_general.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.view_name
        return context

    def dispatch(self, request, *args, **kwargs):
        path = self.request.get_full_path()
        logger.info('anonymous_access {} {}'.format(self.request.META['REMOTE_ADDR'], path))
        return super().dispatch(request, *args, **kwargs)

