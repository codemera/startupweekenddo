from django.contrib import admin
from collaborators.models import (Facilitator, Mentor,
                                  Judges, Organizer, Collaborator,
                                  SponsorCategory, Sponsor, Event)

# Register your models here.

class SponsorCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_order')
    list_display_links = ('name',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_order', 'visible')
    list_display_links = ('name',)

admin.site.register(Event)
admin.site.register(Facilitator)
admin.site.register(Mentor)
admin.site.register(Judges)
admin.site.register(Organizer, PersonAdmin)
admin.site.register(Collaborator)
admin.site.register(SponsorCategory, SponsorCategoryAdmin)
admin.site.register(Sponsor)
