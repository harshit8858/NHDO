from django import forms
from captcha.fields import CaptchaField
from  nhdo_main.models import Profile
from .models import Epin, kyc
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHER', 'other'),
)

class EditForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD', widget=forms.TextInput(attrs={'placeholder':'DOB', 'class':'form-control', 'style':'width:200px'}))
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    referal_id = forms.CharField(help_text='(If any)',required=False,  widget=forms.TextInput(attrs={'placeholder':'Referal_id', 'class':'form-control', 'style':'width:200px'}))
    pan_number = forms.IntegerField(required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder':'Pan Number', 'class':'form-control', 'style':'width:200px'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Address', 'class':'form-control', 'style':'width:200px'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'City', 'class':'form-control', 'style':'width:200px'}))
    pincode = forms.IntegerField(required=True, max_value=999999, widget=forms.NumberInput(attrs={'placeholder':'Pincode', 'class':'form-control', 'style':'width:200px'}))
    mobile_number = forms.IntegerField(required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder':'Mobile Number', 'class':'form-control', 'style':'width:200px'}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'State', 'class':'form-control', 'style':'width:200px'}))
    captcha = CaptchaField()
    profile_pic = forms.FileField(required=False)

    class Meta:
        model = Profile
        fields = ('referal_id',
                  'pan_number',
                  'gender',
                  'birth_date',
                  'address',
                  'city',
                  'pincode',
                  'state',
                  'mobile_number',
                  'profile_pic',
                  'captcha',
                  )

class EditForm1(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control', 'style':'width:200px'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control', 'style':'width:200px'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'E-Mail', 'class':'form-control', 'style':'width:200px'}))

    class Meta:
        model = Profile
        fields = ('first_name',
                  'last_name',
                  'email'
                  )

class Epin_upgradeForm(forms.ModelForm):
    epin = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Enter the new E-Pin', 'class':'form-control', 'style':'width:200px'}))

    class Meta:
        model = Epin
        fields = ['epin']


# class KycForm(UserCreationForm):
class KycForm(forms.ModelForm):
    # username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control', 'style':'width:200px'}))
    dp = forms.FileField(required=True)
    passport = forms.FileField(required=True)
    pan = forms.FileField(required=True)
    aadhar = forms.FileField(required=True)
    voter = forms.FileField(help_text='(Optional)', required=False)
    cancelled_cheque = forms.FileField(help_text='(Optional)',required=False)
    passbook = forms.FileField(required=True)

    class Meta:
        model = kyc
        fields = ['dp', 'passport', 'pan', 'aadhar', 'voter', 'cancelled_cheque', 'passbook']


