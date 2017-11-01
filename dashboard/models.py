from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Epin(models.Model):
    user = models.OneToOneField(User)
    epin = models.CharField(max_length=20)
    tran_number = models.IntegerField()
    tran_date = models.DateField(auto_now=True)
    jo_type = models.CharField(max_length=10)

    def __str__(self):
        return self.epin


class kyc(models.Model):
    user = models.OneToOneField(User, default=None)
    passport = models.FileField(upload_to='passport')
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