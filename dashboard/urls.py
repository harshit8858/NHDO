from django.conf.urls import url
from .views import dashboard, edit_profile, edit_profile1, list_epin, update_kyc, add_kyc, edit_kyc, upgrade_account, welcome_letter, direct_bonus, distributer_agreement, referal_level, referal_team, summary, ac_statement, referal_counts

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'^edit_profile/(\d+)/', edit_profile, name="edit_profile"),
    url(r'^edit_profile1/(\d+)/', edit_profile1, name="edit_profile1"),
    url(r'^list_epin/', list_epin, name="list_epin"),
    url(r'^upgrade_account/', upgrade_account, name="upgrade_account"),
    url(r'^update_kyc/', update_kyc, name="update_kyc"),
    url(r'^add_kyc/', add_kyc, name="add_kyc"),
    url(r'^edit_kyc/(\d+)/', edit_kyc, name="edit_kyc"),
    url(r'^welcome_letter/', welcome_letter, name="welcome_letter"),
    url(r'^distributer_agreement/', distributer_agreement, name="distributer_agreement"),
    url(r'^referal_team/', referal_team, name="referal_team"),
    url(r'^referal_counts/', referal_counts, name="referal_counts"),
    url(r'^referal_level/', referal_level, name="referal_level"),
    url(r'^direct_bonus/', direct_bonus, name="direct_bonus"),
    url(r'^summary/', summary, name="summary"),
    url(r'^ac_statement/', ac_statement, name="ac_statement"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
