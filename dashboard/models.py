from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class kyc(models.Model):
    user = models.OneToOneField(User, default=None)
    passport = models.FileField(upload_to='passport', null=True,blank=True)
    pan = models.FileField(upload_to='pan')
    aadhar = models.FileField(upload_to='aadhar')
    voter = models.FileField(upload_to='voter', blank=True, null=True)
    cancelled_cheque = models.FileField(upload_to='cancelled_cheque', blank=True, null=True)
    passbook = models.FileField(upload_to='passbook')

    def __str__(self):
        return str(self.user)

# @receiver(post_save, sender=User)
# def update_user_kyc(sender, instance, created, **kwargs):
#     if created:
#         kyc.objects.create(user=instance)
#     instance.kyc.save()
#
# post_save.connect(update_user_kyc, sender=User)


class Welcome(models.Model):
    letter =  models.FileField(upload_to='welcome', null=True, blank=True)
    image = models.FileField(upload_to='welcome', null=True, blank=True)


class Distributor_agreement(models.Model):
    d_a = models.FileField(upload_to='distributors_agreement', null=True, blank=True)