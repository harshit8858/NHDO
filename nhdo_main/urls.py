from django.conf.urls import url, include
from .views import *

from .models import Subscription

from newsletter_subscription.backend import ModelBackend
from newsletter_subscription.urls import newsletter_subscriptions_urlpatterns

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'signup/$', signup, name='signup'),
    url(r'^invalid/$', invalid, name="invalid"),
    url(r'^logout/$',logout, name='logout'),
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^auth_check/$', auth_check, name='check'),
    url(r'^home/$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'project/$', project, name='project'),
    url(r'gallery/$', gallery, name='gallery'),
    url(r'contact/$', contact, name='contact'),
    url(r'change_password/$', change_password, name='change_password'),
    url(r'referral_level/$', referral_level, name='referral_level'),
    # url(r'summary/$', summary, name='summary'),

    url(r'women_empowerment/$', women_empowerment, name='women_empowerment'),
    url(r'ierp/$', ierp, name='ierp'),
    url(r'mudra/$', mudra, name='mudra'),
    url(r'shg/$', shg, name='shg'),
    url(r'pmkvy/$', pmkvy , name='pmkvy'),
    url(r'garib_kalyan/$', garib_kalyan, name='garib_kalyan'),
    url(r'standup/$', standup, name='standup'),
    url(r'makeinindia/$', makeinindia, name='makeinindia'),
    url(r'smartcity/$', smartcity, name='smartcity'),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^newsletter/', include(newsletter_subscriptions_urlpatterns(backend=ModelBackend(Subscription), )), name='subscribe' ),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

