from django.urls import path

from ip2location05app.views.FileSubmitView import FileSubmitView
from ip2location05app.views.ResultListView import ResultListView

urlpatterns = [
    path('check', ResultListView.as_view(), name='result_list'),
    path('upload', FileSubmitView.as_view(), name='file_submit'),


]
