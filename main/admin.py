from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Link, Generator


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'img', 'created_at', 'updated_at')
    list_display_links = ('id', 'url', 'img')
    search_fields = ('id', 'url')


admin.site.register(Link, LinkAdmin)


@admin.register(Generator)
class GeneratorAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'img', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'img')
    search_fields = ('id', 'name')
