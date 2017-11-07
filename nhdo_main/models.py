from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from pinax.referrals.models import Referral


GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHER', 'other'),
)


STATUS = (
    ('SINGLE', 'single'),
    ('MARRIED', 'married'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    referal_id = models.CharField(max_length=40, null=True, blank=True)
    pan_number = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    status = models.CharField(max_length=10, choices=STATUS, default='single')
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    profile_pic = models.FileField(upload_to='profile_pic', blank=True, null=True)
    count1 = models.IntegerField(null=True, blank=True, default=0)
    count2 = models.IntegerField(null=True, blank=True, default=0)
    count3 = models.IntegerField(null=True, blank=True, default=0)
    count4 = models.IntegerField(null=True, blank=True, default=0)
    count5 = models.IntegerField(null=True, blank=True, default=0)
    count6 = models.IntegerField(null=True, blank=True, default=0)
    money = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=0)
    total = models.IntegerField(default=0, null=True, blank=True)
    your_referal = models.CharField(max_length=40, default='none')
    level_reached = models.CharField(max_length=20, default=0)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# class Your_referal(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     your_referal = models.CharField(max_length=20)
#
#     def __str__(self):
#         return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    number = models.IntegerField()
    email = models.EmailField()
    query = models.TextField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


from django.db import models
from django.utils.translation import ugettext_lazy as _

from newsletter_subscription.models import SubscriptionBase

class Subscription(SubscriptionBase):
    full_name = models.CharField(_('full name'), max_length=100, blank=True)


# @receiver(user_linked_to_response)
# def handle_user_linked_to_response(sender, response, **kwargs):
#     if response.action == "SOME_SPECIAL_ACTION":
#         pass  # do something with response.user and response.referral.target (object that referral was linked to)