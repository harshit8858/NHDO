from django.contrib import admin
from .models import Profile, Contact, Subscription, Referral


admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Subscription)
admin.site.register(Referral)