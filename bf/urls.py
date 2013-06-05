from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from bf.views import RaceList

urlpatterns = patterns('',
    url(r'^$', login_required(RaceList.as_view())),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', {'login_url': '/accounts/login/?next=/bf/'}),
)