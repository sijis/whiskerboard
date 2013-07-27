from board.models import Service, Status
import datetime
from django.views.generic import ListView, DetailView
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import calendar


class BoardMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BoardMixin, self).get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


def get_past_days(num):
    date = datetime.date.today()
    dates = []

    for i in range(1, num + 1):
        dates.append(date - datetime.timedelta(days=i))

    return dates


class IndexView(BoardMixin, ListView):
    context_object_name = 'services'
    queryset = Service.objects.all()
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['default'] = Status.objects.default()
        context['past'] = get_past_days(5)
        return context


class ServiceView(BoardMixin, DetailView):
    model = Service
    template_name = 'board/service_detail.html'

    def get(self, request, slug=None, year=None, month=None, day=None):

        data = get_object_or_404(self.model, name=slug)

        if year:
            year = int(year)
        if month:
            month = int(month)
        if day:
            day = int(day)

        if day:
            start_date = datetime.date(year, month, day)
            end_date = start_date + datetime.timedelta(days=1)
        elif month:
            start_date = datetime.date(year, month, 1)
            days = calendar.monthrange(start_date.year,
                                       start_date.month)[1]
            end_date = start_date + datetime.timedelta(days=days)
        elif year:
            leap = 366 if calendar.isleap(year) else 365
            start_date = datetime.date(year, 1, 1)
            end_date = start_date + datetime.timedelta(days=leap)
        else:
            # get last 30 days
            start_date = datetime.datetime.now() + datetime.timedelta(days=30)
            end_date = datetime.datetime.now()

        events = data.events.filter(start__gte=start_date).filter(start__lt=end_date)

        no_events = None
        if len(events) == 0:
            no_events = 'No events found.'

        return render_to_response(self.template_name, {
            'service': data,
            'events': events,
            'no_events': no_events,
        }, context_instance=RequestContext(request))
