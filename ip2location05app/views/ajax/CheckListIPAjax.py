from django.http import JsonResponse

from ip2location05app.forms.RecheckResultAjaxForm import RecheckResultAjaxForm
from ip2location05app.models.Result import Result
from ip2location05app.templatetags import extras
from ip2location05app.views.BaseIPCheckView import BaseIPCheckView


class CheckListIPAjax(BaseIPCheckView):
    form_class = RecheckResultAjaxForm

    def form_valid(self, form):
        result_id = form.cleaned_data['result_id']
        result = Result.objects.get(pk=result_id)
        result = self.check_ip(result.address, result.api_configuration, self.request.user, result=result)
        if result.checked:
            data = [
                {
                    'status': 'CHECKED',
                    'result_id': result.pk,
                    'ip': result.address.address,
                    'response': result.response_string,
                    'display_result': extras.show_country(result.response_string)
                }
            ]
        else:
            data = [
                {
                    'status': 'Failed'
                }
            ]

        return JsonResponse(data, safe=False)

