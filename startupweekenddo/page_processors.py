from mezzanine.pages.page_processors import processor_for
from startupweekenddo.models import QuestionCategory
from collections import OrderedDict


@processor_for('startup-weekend')
def add_faq(request, page):
    cats = QuestionCategory.objects.all()
    questions = OrderedDict()

    for cat in cats:
        questions[cat.name] = cat.questions.all()

    return {'faq': questions}
