from django.contrib import admin

from .models import Accident

class AccidentAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'latitude', 'longitude']
    search_fields = ['created_at']

admin.site.register(Accident, AccidentAdmin)