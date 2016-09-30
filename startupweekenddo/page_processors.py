from mezzanine.pages.page_processors import processor_for
from startupweekenddo.models import QuestionCategory, Event, PressRelease
from collections import OrderedDict


@processor_for('startup-weekend')
def add_faq(request, page):
    cats = QuestionCategory.objects.all()
    questions = OrderedDict()

    for cat in cats:
        questions[cat.name] = cat.questions.all()

    return {'faq': questions}


@processor_for('startup-weekend')
def add_events(request, page):
    events = Event.objects.published()[:3]

    return {'past_events': events}


@processor_for('press-kit')
def add_press_releases(request, page):
    releases = PressRelease.objects.filter(published=True)

    return {'press_releases': releases}
