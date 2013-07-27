from tastypie import fields
from tastypie.resources import ModelResource
from board.models import Service, Category, Status, Event
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization


# Authentication class noted from http://stackoverflow.com/a/12273403
class SimpleAuthentication(BasicAuthentication):
    '''
    Authenticates everyone if the request is GET otherwise performs
    BasicAuthentication.
    '''

    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super(SimpleAuthentication, self).is_authenticated(request,
                                                                  **kwargs)


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        excludes = ['id']
        authentication = SimpleAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "name": ALL,
        }


class ServiceResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)

    class Meta:
        queryset = Service.objects.all()
        resource_name = 'services'
        excludes = ['id']
        authentication = SimpleAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "name": ALL,
        }

    def dehydrate(self, bundle):
        # showing latest event for the category
        bundle.data['current-event'] = bundle.obj.current_event()
        return bundle


class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
        excludes = ['id']
        authentication = SimpleAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "name": ALL,
        }


class EventsResource(ModelResource):

    service = fields.ForeignKey(ServiceResource, 'service')
    status = fields.ForeignKey(StatusResource, 'status', full=True)

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        excludes = ['id']
        authentication = SimpleAuthentication()
        authorization = DjangoAuthorization()
