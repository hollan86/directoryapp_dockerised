from django.contrib import admin
from .models import Podcast

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')
    list_filter = ('show',)