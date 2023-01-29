from django.urls import reverse_lazy

from ip2location05app.models.FileInput import FileInput
from ip2location05app.views.HistoryView import HistoryView


class GroupAccessFileHistoryView(HistoryView):
    model = FileInput
    template_name = 'list_file.html'
    view_name = 'Group Access IP File History'
    url_path = reverse_lazy('group_access_result')

    def get_queryset(self):
        return FileInput.objects.filter(
            created_by=self.request.user,
            accessgroup__isnull=False
        ).distinct('pk')

