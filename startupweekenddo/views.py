from mezzanine.utils.views import render
from startupweekenddo.models import Event
from django.db.models import Count, Sum


def index(request):
    context = {
        'events_count': Event.objects.count(),
        'participants_count': 0,
        'cities_count': 0,
        'current_event': Event.objects.published().first(),
    }

    context.update(Event.objects.published().aggregate(participants_count=Sum('participants'),
                                                       cities_count=Count("city")))

    return render(request, "index.html", context)
