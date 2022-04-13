from django.db import models
from django.conf import settings
from .helpers import Base62


class URL(models.Model):
    id = models.AutoField(primary_key=True)
    long_url = models.URLField()
    slug = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def short_url(self):
        return f'{settings.URL_SHORTENER_PREFIX}/{self.slug}'

    def __str__(self):
        return self.long_url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.pk and not self.slug:
            num = self.pk + settings.URL_SHORTENER_SALT
            self.slug = Base62.encode(num)
            self.save()
