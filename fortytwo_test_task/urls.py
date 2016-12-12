from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
from apps.hello.views import HomeView
from apps.requests_history.views import MyRequestHistory
from apps.login.views import MyLoginView

admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^request_history$',MyRequestHistory.as_view(),name = 'request_history'),
    url(r'^registration$',MyLoginView.as_view(),name = 'registration'),
    url(r'^my_login$','apps.login.views.my_registration',name = 'my_login'),
    )
