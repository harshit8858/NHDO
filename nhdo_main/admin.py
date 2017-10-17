from django.contrib import admin
from .models import Profile, Contact, Subscription


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile_number','referal_id')

    def get_list_filter(self, request):        #1
        if request.user.is_superuser:
            return ['user', 'referal_id']
        else:
            return []
admin.site.register(Profile, ProfileAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'done', 'email')

    def get_list_filter(self, request):        #1
        if request.user.is_superuser:
            return ['name', 'done']
        else:
            return []
admin.site.register(Contact, ContactAdmin)

admin.site.register(Subscription)

