from django.conf.urls import url
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^blog_delete/(\d+)/', blog_delete, name='blog_delete'),
    url(r'^blog_edit/(\d+)/', blog_edit, name='blog_edit'),
    url(r'^blog_search/', blog_search, name='blog_search'),
    url(r'^blog_comment/', blog_comment, name='blog_comment'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

