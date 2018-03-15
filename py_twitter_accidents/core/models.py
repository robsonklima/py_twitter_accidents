from django.db import models

class Accident(models.Model):
    occurred_at = models.DateField('Ocurred At', null=True, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    latitude = models.CharField('Latitude', max_length=40)
    longitude = models.CharField('Longitude', max_length=40)
    is_open_data = models.BooleanField('Is Open Data', default=False)
    is_twitter = models.BooleanField('Is Twitter', default=False)

    def __str__(self):
        return self.occurred_at

    class Meta:
        verbose_name = "Accident"
        verbose_name_plural = "Accidents"
        ordering = ['occurred_at']
