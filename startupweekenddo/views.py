from startupweekenddo.models import Event
from django.db.models import Count, Sum
from django.template.response import TemplateResponse


def index(request):

    current_event = Event.objects.published().first()
    schedule_days = None
    try:
        if current_event:
            schedule_days = current_event.schedule.scheduleitem_set.all().datetimes('time', 'day')
    except Exception:
        # Event has no schedule
        schedule_days = None

    context = {
        'events_count': Event.objects.published().count(),
        'participants_count': 0,
        'cities_count': 0,
        'current_event': current_event,
        'schedule_days': schedule_days,
    }

    context.update(Event.objects.published().aggregate(participants_count=Sum('participants'),
                                                       cities_count=Count("city")))

    return TemplateResponse(request, "index.html", context)
