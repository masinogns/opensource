from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

class Community(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_date = models.DateTimeField( #날째
            blank=True, null=True, auto_now_add = True);

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title
