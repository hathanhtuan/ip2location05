from django.urls import reverse_lazy

from ip2location05app.models.FileInput import FileInput
from ip2location05app.views.HistoryView import HistoryView


class GroupAccessFileHistoryView(HistoryView):
    model = FileInput
    paginate_by = 200
    template_name = 'list_file.html'
    view_name = 'Group Access IP File History - need a distinct query,' \
                ' this demo site is backed by sqlite so it is impossible'
    url_path = reverse_lazy('group_access_result')

    def get_queryset(self):
        return FileInput.objects.filter(
            created_by=self.request.user,
            accessgroup__isnull=False
        ).order_by('-created_at')

