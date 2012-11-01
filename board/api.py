from tastypie import fields
from tastypie.resources import ModelResource
from board.models import Service, Category, Status, Event

class ServiceResource(ModelResource):
    class Meta:
        queryset = Service.objects.all()
        resource_name = 'services'
        excludes = ['slug']

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        excludes = ['slug']

class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
        excludes = ['slug']

class EventsResource(ModelResource):

    service = fields.ForeignKey(ServiceResource, 'service')
    status = fields.ForeignKey(StatusResource, 'status')

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        excludes = ['slug']

