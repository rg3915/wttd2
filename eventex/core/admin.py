from django.contrib import admin
from eventex.core.models import Speaker


class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

admin.site.register(Speaker, SpeakerModelAdmin)
