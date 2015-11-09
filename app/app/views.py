from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from collaborators.models import (Facilitator, Mentor,
                                  Judges, Organizer, Sponsor,
                                  Event, Collaborator)


def home(request):
    facilitators = Facilitator.objects.all()[:1]
    mentors = Mentor.objects.all()
    judges = Judges.objects.all()
    organizer = Organizer.objects.all()
    collaborators = Collaborator.objects.all()

    # sponsors categori
    diamond = Sponsor.objects.filter(categori__number_order=1).all()
    platinum = Sponsor.objects.filter(categori__number_order=2).all()
    gold = Sponsor.objects.filter(categori__number_order=3).all()
    silver = Sponsor.objects.filter(categori__number_order=4).all()
    bronze = Sponsor.objects.filter(categori__number_order=5).all()
    media_partner = Sponsor.objects.filter(categori__number_order=6).all()

    sponsors = {'diamonds': diamond,
                'platinums': platinum,
                'golds': gold,
                'silvers': silver,
                'bronzes': bronze,
                'media_partners': media_partner}

    event = Event.objects.all()[:1]

    content = {'facilitators': facilitators,
               'mentors': mentors,
               'judges': judges,
               'organizer': organizer,
               'sponsors': sponsors,
               'collaborators': collaborators,
               'event': event[0]}

    return render_to_response('base.html', content)
