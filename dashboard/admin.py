from django.contrib import admin
from .models import kyc, Welcome, Distributor_agreement


class kycAdmin(admin.ModelAdmin):
    list_display = ('user', 'aadhar')

    def get_list_filter(self, request):        #1
        if request.user.is_superuser:
            return ['user']
        else:
            return []
admin.site.register(kyc, kycAdmin)

admin.site.register(Welcome)

admin.site.register(Distributor_agreement)
