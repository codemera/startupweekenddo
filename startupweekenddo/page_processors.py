from mezzanine.pages.page_processors import processor_for
from startupweekenddo.models import QuestionCategory, Event
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
