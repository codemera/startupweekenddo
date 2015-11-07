from django.contrib import admin
from collaborators.models import (Facilitator, Mentor,
                                  Judges, Organizer, Collaborator,
                                  SponsorCategory, Sponsor, Event)

# Register your models here.

admin.site.register(Facilitator)
admin.site.register(Mentor)
admin.site.register(Judges)
admin.site.register(Organizer)
admin.site.register(Collaborator)
admin.site.register(SponsorCategory)
admin.site.register(Sponsor)
admin.site.register(Event)
