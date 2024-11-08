from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Generator)
class GeneratorTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


