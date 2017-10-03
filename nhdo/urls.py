from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('nhdo_main.urls')),
    url(r'^password_reset/', include('nhdo_reset.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^referrals/', include('pinax.referrals.urls')),

]
