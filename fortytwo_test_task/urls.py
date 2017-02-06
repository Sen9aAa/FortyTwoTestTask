from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
from apps.hello.views import HomeView
from apps.requests_history.views import MyRequestHistory
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^request_history$',MyRequestHistory.as_view(),name = 'request_history'),
    url(r'^add_data$','apps.hello.views.my_add_data_form',name = 'add_data'),    
    url(r'^my_registration$','apps.login.views.my_registration',name = 'my_registration'),
    url(r'^my_login$','apps.login.views.my_login',name = 'my_login'),
    url(r'^my_logout$','apps.login.views.my_logout',name = 'my_logout'),
    url(r'^my_delete/(?P<my_info_id>\d+)/$','apps.hello.views.my_delete',name = 'my_delete'),
    url(r'^my_change/(?P<info_id>\d+)/$','apps.hello.views.my_add_data_form',name = 'my_change'),
    )
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

