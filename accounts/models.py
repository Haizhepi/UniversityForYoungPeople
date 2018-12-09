from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime


class UserProfile(models.Model):
        user = models.OneToOneField(User)
        middle = models.CharField(max_length=100, default='', blank=True)
        suffix = models.CharField(max_length=100, default='', blank=True)
        address1 = models.CharField(max_length=100, default='')
        address2 = models.CharField(max_length=100, default='', blank=True)
        city = models.CharField(max_length=100, default='')
        state = models.CharField(max_length=100, default='')
        zip = models.IntegerField(default=0)
        phone = models.BigIntegerField(default=0)
        grad_year = models.IntegerField(default=2020)
        birth_date = models.DateField(default=datetime.date.today)
        yes_or_no_unsure = (
            ('Y', 'Yes'),
            ('N', 'No'),
            ('U', 'Unsure'),
        )
        yes_or_no = (
            ('Y', 'Yes'),
            ('N', 'No'),
        )
        accepted_to_GT_program = models.CharField(max_length=1, choices=yes_or_no_unsure, default='N')
        english_learn = models.CharField(max_length=1, choices=yes_or_no, default='Y')
        approved_to_register = models.CharField(max_length=1, choices=yes_or_no, default='N')

        def __str__(self):
            return self.user.username + "'s profile"


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)