from django.urls import path

from ip2location05app.views.CheckSingleIPView import CheckSingleIPView
from ip2location05app.views.ExternalToolFacebookSearchView import ExternalToolFacebookSearchView
from ip2location05app.views.ExternalToolView import ExternalToolView
from ip2location05app.views.FileHistoryView import FileHistoryView
from ip2location05app.views.FileSubmitView import FileSubmitView
from ip2location05app.views.GroupAccessByIPResultView import GroupAccessByIPResultView
from ip2location05app.views.GroupAccessByIPView import GroupAccessByIPView
from ip2location05app.views.GroupAccessFileHistoryView import GroupAccessFileHistoryView
from ip2location05app.views.SingleIPHistoryView import SingleIPHistoryView
from ip2location05app.views.ajax.CheckListIPAjax import CheckListIPAjax

urlpatterns = [
    # path('check', ResultListView.as_view(), name='result_list'),
    path('upload', FileSubmitView.as_view(), name='file_submit'),
    path('single', CheckSingleIPView.as_view(), name='single_ip_submit'),
    path('history_ip', SingleIPHistoryView.as_view(), name='history_ip'),
    path('history_file', FileHistoryView.as_view(), name='history_file'),
    path('group_access', GroupAccessByIPView.as_view(), name='group_access'),
    path('group_access_result', GroupAccessByIPResultView.as_view(), name='group_access_result'),
    path('list_group_access_file', GroupAccessFileHistoryView.as_view(), name='group_access_file'),
    path('tool/facebook', ExternalToolFacebookSearchView.as_view(), name='external_tool_facebook'),
    path('tool', ExternalToolView.as_view(), name='external_tool'),
    path('ajax/chek_ip', CheckListIPAjax.as_view(), name='ajax_check_ip'),
]
