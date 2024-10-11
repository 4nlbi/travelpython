from django.contrib import admin

from . models import services

from . models import portfolio

from . models import story

# Register your models here.
admin.site.register(services)
admin.site.register(portfolio)
admin.site.register(story)

