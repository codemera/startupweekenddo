from startupweekenddo.models import Event, HomePageData
from django.db.models import Count, Sum
from django.db.models import Q
from django.template.response import TemplateResponse
from startupweekenddo.utils import localized_date
from collections import OrderedDict


def index(request):
    today = localized_date()
    query = Q(start_date__gte=today) | Q(start_date__lte=today, end_date__gte=today)
    current_event = Event.objects.published().filter(query).first()
    schedule_days = OrderedDict()
    try:
        if current_event:
            items = current_event.schedule.items.all()
            for item in items:
                date = localized_date(item.time).date()
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
        'latest_events':  Event.objects.published()[:6],
    }

    context.update(Event.objects.published().aggregate(participants_count=Sum('participants'),
                                                       cities_count=Count("city")))

    return TemplateResponse(request, "index.html", context)
