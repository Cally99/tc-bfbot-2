from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from bf.views import RaceList

urlpatterns = patterns('',
    url(r'^$', login_required(RaceList.as_view())),
)