from django.contrib import admin
from .models import Epin, kyc, Welcome


admin.site.register(Epin)

class kycAdmin(admin.ModelAdmin):
    list_display = ('user', 'pan')

    def get_list_filter(self, request):        #1
        if request.user.is_superuser:
            return ['user']
        else:
            return []
admin.site.register(kyc, kycAdmin)

admin.site.register(Welcome)