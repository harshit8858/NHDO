from django.contrib import admin
from .models import Profile, Contact, Subscription


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile_number', 'your_referal', 'referal_id', 'level_reached')

    def get_list_filter(self, request):        #1
        if request.user.is_superuser:
            return ['user', 'referal_id']
        else:
            return []
admin.site.register(Profile, ProfileAdmin)


# class Your_referalAdmin(admin.ModelAdmin):
#     list_display = ('user', 'your_referal')
#
#     def get_list_filter(self, request):
#         if request.user.is_superuser:
#             return ['user', 'your_referal']
#         else:
#             return[]
# admin.site.register(Your_referal, Your_referalAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'done', 'email')

    def get_list_filter(self, request):        #1
        if request.user.is_superuser:
            return ['name', 'done']
        else:
            return []
admin.site.register(Contact, ContactAdmin)

admin.site.register(Subscription)

