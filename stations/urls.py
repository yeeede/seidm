from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns
from stations import views

urlpatterns = [ 
    url(r'^stations/$', views.StationList.as_view()),
    url(r'^stations/(?P<pk>[0-9]+)/$', views.StationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
