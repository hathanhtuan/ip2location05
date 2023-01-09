from ip2location05app.models.Result import Result
from ip2location05app.views.HistoryView import HistoryView


class SingleIPHistoryView(HistoryView):
    model = Result
    paginate_by = 200
    template_name = 'list_result.html'
    view_name = 'IP history check'

    def get_queryset(self):
        single_ip = self.request.GET.get('ip', False)
        file_ip = self.request.GET.get('file', False)
        if single_ip:
            return Result.objects.filter(address__address=single_ip, created_by=self.request.user)\
                .order_by('-created_at')
        elif file_ip:
            file_ip = int(file_ip)
            return Result.objects.filter(fileinput=file_ip, created_by=self.request.user)\
                .order_by('-created_at')
        else:
            return Result.objects.filter(created_by=self.request.user).order_by('-created_at')

