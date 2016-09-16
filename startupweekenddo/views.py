from mezzanine.utils.views import render
from startupweekenddo.models import Event
from django.db.models import Count, Sum


def index(request):

    current_event = Event.objects.published().first()
    schedule_days = current_event.schedule.scheduleitem_set.all().datetimes('time', 'day')

    context = {
        'events_count': Event.objects.count(),
        'participants_count': 0,
        'cities_count': 0,
        'current_event': current_event,
        'schedule_days': schedule_days,
    }

    context.update(Event.objects.published().aggregate(participants_count=Sum('participants'),
                                                       cities_count=Count("city")))

    return render(request, "index.html", context)
