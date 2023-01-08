from django.views.generic import ListView

from ip2location05app.models.Result import Result
from ip2location05app.views.BaseView import BaseView


class ResultListView(BaseView, ListView):
    model = Result
    template_name = 'list_result.html'
    view_name = 'IP check results'

    def get_queryset(self):
        file_id = self.request.GET.get('file_id', False)
        file_id = int(file_id)
        if file_id:
            return Result.objects.filter(address__fileinput=file_id)
        else:
            return Result.objects.none()
