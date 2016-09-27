from startupweekenddo.models import Event, HomePageData
from django.db.models import Count, Sum
from django.template.response import TemplateResponse
from collections import OrderedDict


def index(request):
    current_event = Event.objects.published().first()
    schedule_days = OrderedDict()
    try:
        if current_event:
            items = current_event.schedule.items.all()
            for item in items:
                date = item.time.date()
                if date not in schedule_days:
                    schedule_days[date] = [item]
                else:
                    schedule_days[date].append(item)
    except Exception:
        # Event has no schedule
        schedule_days = {}

    context = {
        'events_count': Event.objects.published().count(),
        'participants_count': 0,
        'cities_count': 0,
        'current_event': current_event,
        'schedule_days': schedule_days,
        'homepagedata': HomePageData.objects.first(),
    }

    context.update(Event.objects.published().aggregate(participants_count=Sum('participants'),
                                                       cities_count=Count("city")))

    return TemplateResponse(request, "index.html", context)
