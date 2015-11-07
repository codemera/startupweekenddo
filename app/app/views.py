from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from collaborators.models import (Facilitator, Mentor,
                                  Judges, Organizer, Sponsor,
                                  Event)


def home(request):
    facilitators = Facilitator.objects.all()
    mentors = Mentor.objects.all()
    judges = Judges.objects.all()
    organizer = Organizer.objects.all()

    # sponsors categori
    diamond = Sponsor.objects.filter(categori__name='diamante').all()
    platinum = Sponsor.objects.filter(categori__name='platinum').all()
    gold = Sponsor.objects.filter(categori__name='gold').all()
    silver = Sponsor.objects.filter(categori__name='silver').all()
    bronze = Sponsor.objects.filter(categori__name='bronze').all()
    media_partner = Sponsor.objects.filter(categori__name='media pathner').all()

    sponsors = {'diamonds': diamond,
                'platinums': platinum,
                'golds': gold,
                'silvers': silver,
                'bronzes': bronze,
                'media_partners': media_partner}

    event = Event.objects.first()

    content = {'facilitators': facilitators,
               'mentors': mentors,
               'judges': judges,
               'organizer': organizer,
               'sponsors': sponsors,
               'event': event}

    return render_to_response('base.html', content)
