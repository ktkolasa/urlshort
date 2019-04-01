from django.db import models

class FullURL(models.Model):
    full_url_string = models.CharField(max_length=500)
    short_url = models.CharField(max_length=50, default=None)
    
    def __str__(self):
        return self.full_url_string
