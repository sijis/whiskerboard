from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from board.feeds import EventFeed
from board.views import IndexView, ServiceView
from board.api import ServiceResource, CategoryResource, StatusResource, EventsResource
from tastypie.api import Api

admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(ServiceResource())
v1_api.register(CategoryResource())
v1_api.register(StatusResource())
v1_api.register(EventsResource())

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^services/(?P<slug>[-\w]+)$', ServiceView.as_view(), name='service'),
    url(r'^feed$', EventFeed(), name='feed'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

