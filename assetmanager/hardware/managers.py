#hardware/managers.py
from django.utils.translation import ugettext_lazy as _
from django.db import models

from django.db.models import Q # new
from itertools import chain



class HardwareManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(asset_tag__icontains=query) |
                         Q(notes__icontains=query) |
                         Q(ip_address__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
