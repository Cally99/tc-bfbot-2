from django.urls import include, path
from django.contrib import admin
import django.contrib.auth.views as auth_views
admin.autodiscover()

urlpatterns = [
    path('bf/', 'bf.urls'),
    path('admin/', admin.site.urls),
    path('accounts/login/$', auth_views.login),
]
