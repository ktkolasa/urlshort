from django.contrib import admin
from .models import FullURL 

class UrlsAdmin(admin.ModelAdmin):
    #fields= ['full_url_string', 'short_url']
    fieldsets = [
        (None,               {'fields': ['full_url_string']}),
        ('Date information', {'fields': ['short_url'] }),
    ]
    list_display = ('full_url_string','short_url')

    
admin.site.register(FullURL, UrlsAdmin)