from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import ContactForm
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMessage
from pinax.referrals.models import Referral
import pinax
from django.contrib.auth.models import User



def index(request):
    # email = EmailMessage('title', 'body', to=['dk291996@gmail.com'])
    # abc = email.send()
    # print (abc)
    return render(request, 'index.html')


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.first_name = form.cleaned_data.get('firts_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.referal_id = form.cleaned_data.get('referal_id')
            user.profile.pan_number = form.cleaned_data.get('pan_number')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.mobile_number = form.cleaned_data.get('mobile_number')
            user.profile.pincode = form.cleaned_data.get('pincode')
            user.profile.email_id = form.cleaned_data.get('email_id')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.profile_pic = form.cleaned_data.get('profile_pic')
            user.save()
            referral = Referral.create(
                user=user,
                redirect_to=reverse("index")
            )
            Profile.referral = referral
            print("h")
            # Profile.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def your_referal(request):
    referral = Referral.objects.all()
    # r = pinax.referrals.objects.all()
    # u = User.objects.all()
    referral_response = Referral.record_response(request, "SOME_ACTION")
    return render(request, 'your_referal.html', {'referral_response':referral_response, 'referral':referral })


def auth_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('home')
    else:
        return HttpResponseRedirect('/invalid/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def invalid(request):
    return render(request, 'invalid.html')


def log_in(request):
    return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return render(request, 'invalid.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    # n = Profile.objects.filter()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})


def change_password(request):
    user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            #new_password = form.cleaned_data['new_password']
            #user.set_password(new_password)
            #user.save()
            form.save()
            return redirect('index')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


# def captcha(request):
#     if request.POST:
#         form = CaptchaTestForm(request.POST)
#
#         # Validate the form: the captcha field will automatically
#         # check the input
#         if form.is_valid():
#             human = True
#     else:
#         form = CaptchaTestForm()
#
#     return render_to_response('template.html',locals())

# from django.views.generic.edit import CreateView
# from captcha.models import CaptchaStore
# from captcha.helpers import captcha_image_url
# from django.http import HttpResponse
# import json
# from .forms import CaptchaTestForm
#
# class AjaxExampleForm(CreateView):
#     template_name = ''
#     form_class = CaptchaTestForm
#
#     def form_invalid(self, form):
#         if self.request.is_ajax():
#             to_json_response = dict()
#             to_json_response['status'] = 0
#             to_json_response['form_errors'] = form.errors
#
#             to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
#             to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])
#
#             return HttpResponse(json.dumps(to_json_response), content_type='application/json')
#
#     def form_valid(self, form):
#         form.save()
#         if self.request.is_ajax():
#             to_json_response = dict()
#             to_json_response['status'] = 1
#
#             to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
#             to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])
#
#             return HttpResponse(json.dumps(to_json_response), content_type='application/json')