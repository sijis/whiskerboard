from tastypie import fields
from tastypie.resources import ModelResource
from board.models import Service, Category, Status, Event
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        excludes = ['slug', 'id']
        filtering = {
            "name": ALL,
        }


class ServiceResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)

    class Meta:
        queryset = Service.objects.all()
        resource_name = 'services'
        excludes = ['slug', 'id']
        filtering = {
            "name": ALL,
        }

    def dehydrate(self, bundle):
        # showing latest event for the category
        bundle.data['current-event'] = bundle.obj.current_event()
        return bundle.data

class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
        excludes = ['slug', 'id']
        filtering = {
            "name": ALL,
        }


class EventsResource(ModelResource):

    #service = fields.ForeignKey(ServiceResource, 'service', full=True)
    status = fields.ForeignKey(StatusResource, 'status', full=True)

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        excludes = ['slug', 'id']

