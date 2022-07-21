#hardware/models
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
from .managers import HardwareManager
from people.models import User
from status_labels.models import Status_label
from companies.models import Company
from locations.models import Location

class Hardware(models.Model):
    # fields
    order_id = models.IntegerField(default=1)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this Asset.', editable=False, unique=True)
    name = models.CharField(max_length=50, default='', help_text="Enter the Asset's Name")
    asset_tag = models.CharField(max_length=200, default='', help_text="Enter the Asset's Asset Tag.")
    ip_address = models.GenericIPAddressField()
    purchase_date = models.DateField(default=datetime.date.today, help_text="Enter the date the Asset was purchased.")
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    assigned_to = models.ForeignKey(User, related_name='+', default='', on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, related_name='+', default='', on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, related_name='+', default='', on_delete=models.CASCADE)
    notes = models.CharField(max_length=2000, default='', help_text="Enter notes for the Asset.")
    physical = models.BooleanField(default=False, help_text="Is the Asset physical?", null=True)
    categorization = models.CharField(max_length=50, default='', help_text="Enter the Asset's Security Categorization")
    status_id = models.ForeignKey(Status_label, related_name='+', default='', on_delete=models.CASCADE)
    objects = HardwareManager()

    # Metadata
    class Meta:
        ordering = ['order_id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = Hardware.objects.all().aggregate(largest=models.Max('order_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.order_id = last_id + 1
        super(Hardware, self).save(*args, **kwargs)