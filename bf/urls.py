from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
import django.contrib.auth.views as auth_views

from bf.views import RaceList




urlpatterns = [
    path('', login_required(RaceList.as_view())),
    path('logout/' , auth_views.logout,  {'login_url': '/accounts/login/?next=/bf/'}) ,
]


'''

urlpatterns = [
    url(r'^$', login_required(RaceList.as_view())),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', {'login_url': '/accounts/login/?next=/bf/'}),
]


from posts.views import post_home

urlpatterns = [
    ...
    url(r'^posts/$', post_home),
]

urlpatterns = patterns('',
    url(r'^bf/', include('bf.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

'''
