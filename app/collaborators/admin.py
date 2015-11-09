from django.contrib import admin
from collaborators.models import (Facilitator, Mentor,
                                  Judges, Organizer, Collaborator,
                                  SponsorCategory, Sponsor, Event)

# Register your models here.

class SponsorCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_order')
    list_display_links = ('name',)


admin.site.register(Facilitator)
admin.site.register(Mentor)
admin.site.register(Judges)
admin.site.register(Organizer)
admin.site.register(Collaborator)
admin.site.register(SponsorCategory, SponsorCategoryAdmin)
admin.site.register(Sponsor)
admin.site.register(Event)
