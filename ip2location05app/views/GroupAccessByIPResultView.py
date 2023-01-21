from ip2location05app.models.AccessGroup import AccessGroup
from ip2location05app.views.HistoryView import HistoryView


class GroupAccessByIPResultView(HistoryView):
    view_name = 'Group Access By IP Result View'
    template_name = 'list_access_group.html'

    def get_queryset(self):
        file_log = self.request.GET.get('file', False)
        file_log_id = int(file_log)
        if file_log_id:
            return AccessGroup.objects.filter(file_input_id=file_log_id)
        else:
            return AccessGroup.objects.none()

