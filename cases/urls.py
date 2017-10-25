from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cases import views

urlpatterns = [
    url(r'^cases/$', views.CaseList.as_view()),
    url(r'^cases/(?P<pk>[0-9]+)/$', views.CaseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
