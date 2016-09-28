from mezzanine.pages.page_processors import processor_for
from startupweekenddo.models import Question, Event


@processor_for('startup-weekend')
def add_faq(request, page):
    questions = Question.objects.all()

    return {'faq': questions}

@processor_for('startup-weekend')
def add_events(request, page):
    events = Event.objects.published()[:3]

    return {'past_events': events}
