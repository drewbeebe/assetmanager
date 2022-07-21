#people/models.py
import datetime
import uuid
from . import cipher

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator, validate_email, EmailValidator
from django.utils import timezone

# local imports
from .utils import AESCipher

#encryption Import
from django.db.models.fields import CharField, AutoField

##imports for People
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .managers import UserManager
from companies.models import Company
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import hashers
from django.conf import settings
### classes for re-formatting models below

# EncryptedField
class EnField(CharField):
    def from_db_value(self, value, expression, connection):
        """ Decrypt the data for display in Django as normal. """
        #return cipher.decrypt(value)
        encryption_key = getattr(settings, 'SECRET_KEY', None)
        return AESCipher(encryption_key).decrypt(value).decode('utf-8')
    def get_prep_value(self, value):
        """ Encrypt the data when saving it into the database. """
        #return cipher.encrypt(value)
        encryption_key = getattr(settings, 'SECRET_KEY', None)
        return AESCipher(encryption_key).encrypt(value).decode('utf-8')

class User(AbstractBaseUser, PermissionsMixin):
    order_id = models.IntegerField(default=1)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this User.', editable=False, unique=True)
    first_name = models.CharField(_('first name'), max_length=500, blank=False)
    last_name = models.CharField(_('last name'), max_length=500, blank=False)
    usercompany = models.ManyToManyField(Company, through='CompanyUsers', blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
    )
    is_active = models.BooleanField(default=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups   = models.ManyToManyField(Group, blank=True, default=1, related_name='group')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ ] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = User.objects.all().aggregate(largest=models.Max('order_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.order_id = last_id + 1
        super(User, self).save(*args, **kwargs)


class CompanyUsers(models.Model):
    Company = models.ForeignKey(Company, related_name='+', on_delete=models.CASCADE)
    User = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)