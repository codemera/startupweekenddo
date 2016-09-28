from mezzanine.pages.page_processors import processor_for
from startupweekenddo.models import Question


@processor_for('startup-weekend')
def add_faq(request, page):
    questions = Question.objects.all()

    return {'faq': questions}
