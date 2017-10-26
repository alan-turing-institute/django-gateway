from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from jobs import views

urlpatterns = [
    url(r'^jobs/$', views.JobList.as_view()),
    url(r'^jobs/(?P<pk>[0-9]+)/$', views.JobDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
