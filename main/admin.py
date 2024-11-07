from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'img', 'created_at', 'updated_at')
    list_display_links = ('id', 'url', 'img')
    search_fields = ('id', 'url')


admin.site.register(Link, LinkAdmin)


