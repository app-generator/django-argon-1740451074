# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Checkin(models.Model):

    #__Checkin_FIELDS__
    arrival = models.DateTimeField(blank=True, null=True, default=timezone.now)
    departure = models.DateTimeField(blank=True, null=True, default=timezone.now)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    folio_id = models.ForeignKey(Folio, on_delete=models.CASCADE)

    #__Checkin_FIELDS__END

    class Meta:
        verbose_name        = _("Checkin")
        verbose_name_plural = _("Checkin")


class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    ic_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Reservation(models.Model):

    #__Reservation_FIELDS__
    arrival = models.DateTimeField(blank=True, null=True, default=timezone.now)
    departure = models.DateTimeField(blank=True, null=True, default=timezone.now)
    rate_type = models.CharField(max_length=255, null=True, blank=True)
    market_segment = models.CharField(max_length=255, null=True, blank=True)
    source_of_business = models.CharField(max_length=255, null=True, blank=True)
    total_charges = models.IntegerField(null=True, blank=True)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    number_of_rooms = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField()
    email = models.CharField(max_length=255, null=True, blank=True)
    guestname1 = models.CharField(max_length=255, null=True, blank=True)
    guestname2 = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    telnumber = models.CharField(max_length=255, null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)

    #__Reservation_FIELDS__END

    class Meta:
        verbose_name        = _("Reservation")
        verbose_name_plural = _("Reservation")


class Folio(models.Model):

    #__Folio_FIELDS__
    folio_number = models.CharField(max_length=255, null=True, blank=True)
    rate_type = models.CharField(max_length=255, null=True, blank=True)
    total_charges = models.IntegerField(null=True, blank=True)
    vehicle_number = models.CharField(max_length=255, null=True, blank=True)
    market_segment = models.CharField(max_length=255, null=True, blank=True)
    source_of_business = models.CharField(max_length=255, null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deposit = models.IntegerField(null=True, blank=True)
    master_folio_id = models.ForeignKey(MasterFolio, on_delete=models.CASCADE)

    #__Folio_FIELDS__END

    class Meta:
        verbose_name        = _("Folio")
        verbose_name_plural = _("Folio")


class Masterfolio(models.Model):

    #__Masterfolio_FIELDS__
    master_folio_number = models.CharField(max_length=255, null=True, blank=True)

    #__Masterfolio_FIELDS__END

    class Meta:
        verbose_name        = _("Masterfolio")
        verbose_name_plural = _("Masterfolio")



#__MODELS__END
