from django.conf.urls import url
from .views import dashboard, edit_profile, edit_profile1, list_epin, update_kyc, add_kyc, edit_kyc, upgrade_account, welcome_letter, direct_bonus, distributer_agreement, downline_team, geneology_team, compose, referal_team, summary, ac_statement

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'^edit/(\d+)/', edit_profile, name="edit"),
    url(r'^edit1/(\d+)/', edit_profile1, name="edit1"),
    url(r'^list_epin/', list_epin, name="list_epin"),
    url(r'^upgrade_account/', upgrade_account, name="upgrade_account"),
    url(r'^update_kyc/', update_kyc, name="update_kyc"),
    url(r'^add_kyc/', add_kyc, name="add_kyc"),
    url(r'^edit_kyc/(\d+)/', edit_kyc, name="edit_kyc"),
    url(r'^welcome_letter/', welcome_letter, name="welcome_letter"),
    url(r'^distributer_agreement/', distributer_agreement, name="distributer_agreement"),
    url(r'^geneology_team/', geneology_team, name="geneology_team"),
    url(r'^referal_team/', referal_team, name="referal_team"),
    url(r'^downline_team/', downline_team, name="downline_team"),
    url(r'^direct_bonus/', direct_bonus, name="direct_bonus"),
    url(r'^summary/', summary, name="summary"),
    url(r'^ac_statement/', ac_statement, name="ac_statement"),
    url(r'^compose/', compose, name="compose"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
