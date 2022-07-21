#status_labels/models
from django.db import models

# Create your models here.
import datetime
import uuid
from itertools import chain


#imports for django
from django.db import models
from django.db.models import F, Q # new
from django.db.models.signals import post_save

#from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, validate_email
from django.core.files.storage import FileSystemStorage, get_storage_class
from django.conf.urls.static import static
from django.dispatch import receiver

#local imports
from .managers import Status_labelManager


class Status_label(models.Model):
    # fields
    order_id = models.IntegerField(default=1)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this Location.', editable=False, unique=True)
    name = models.CharField(max_length=500, default='', help_text="Enter the Location's Name")
    objects = Status_labelManager()

    # Metadata
    class Meta:
        ordering = ['order_id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = Status_label.objects.all().aggregate(largest=models.Max('order_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.order_id = last_id + 1
        super(Status_label, self).save(*args, **kwargs)