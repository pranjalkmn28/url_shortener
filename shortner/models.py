from django.db import models
from django.utils import timezone
import string
import random
from datetime import timedelta
from django.core.exceptions import ValidationError


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class URL(TimestampedModel):
    original_url = models.URLField(max_length=2048)
    short_url = models.CharField(max_length=10)
    alias = models.CharField(max_length=10, null=True, blank=True)
    expiry_time = models.IntegerField(help_text="Expiry time in minutes", null=True, blank=True)

    def __str__(self):
        return f"url - {self.original_url}, expired - {str(self.is_expired)}"

    def save(self, *args, **kwargs):
        '''
            1. check if custom alias is given by user.
            2. if not given then generate short url.
            3. if given then alias availablity.
        '''
        if not self.alias:
            self.short_url = self.generate_short_code()
        else:
            alias_availability = self.check_alias_availability(self.alias)
            if alias_availability:
                self.short_url = self.alias
        
        # if expiry time is not given then default expiry time is 24 hours.
        if not self.expiry_time:
            self.expiry_time = 1440
        super().save(*args, **kwargs)

    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choices(characters, k=length))
            if not URL.objects.filter(short_url=short_code).exists():
                break
        return short_code


    def check_alias_availability(self, alias):
        """
        Check if any non-expired URL with the given alias already exists.
        Raise a ValidationError if such a URL exists.
        """
        existing_url = URL.objects.filter(alias=alias).order_by('-created_at').first()
        if existing_url and not existing_url.is_expired:
            raise ValidationError(f"The alias '{alias}' is already in use.")
            return False
        return True
        
    @property
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=self.expiry_time)
    