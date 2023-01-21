from django.urls import reverse, reverse_lazy

from ip2location05app.models.FileInput import FileInput
from ip2location05app.views.HistoryView import HistoryView


class FileHistoryView(HistoryView):
    model = FileInput
    paginate_by = 200
    template_name = 'list_file.html'
    view_name = 'File history check'
    url_path = reverse_lazy('history_ip')

    def get_queryset(self):
        return FileInput.objects.filter(created_by=self.request.user).order_by('-created_at')

