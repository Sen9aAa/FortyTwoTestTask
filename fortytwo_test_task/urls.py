from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.hello.views import HomeView
from apps.requests_history.views import MyRequestHistory
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^request_history$',MyRequestHistory.as_view(),name = 'request_history'),
    )
