import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

logger = logging.getLogger(__name__)


class BaseView(LoginRequiredMixin, View):
    view_name = 'Default View Namee'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        path = self.request.get_full_path()
        logger.info('user_access {} {} {}'.format(self.request.META['REMOTE_ADDR'], user, path))
        return super().dispatch(request, *args, **kwargs)

