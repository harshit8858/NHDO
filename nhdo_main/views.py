from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import ContactForm
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from dashboard.views import referal_level, referal_counts, referal_team, summary


amount = 500


def index(request):
    home(request)
    nom = Profile.objects.all()
    nav1 = "active"
    return render(request, 'nhdo_main/index.html', {'nom':nom, 'nav1':nav1})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.pan_number = form.cleaned_data.get('pan_number')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.pincode = form.cleaned_data.get('pincode')
            user.profile.email_id = form.cleaned_data.get('email_id')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.profile_pic = form.cleaned_data.get('profile_pic')
            user.profile.referal_id = form.cleaned_data.get('referal_id')
            user.profile.mobile_number = form.cleaned_data.get('mobile_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth.login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    rnav = "active"
    return render(request, 'nhdo_main/signup.html', {'form':form, 'rnav':rnav})


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
    return render(request, 'nhdo_main/invalid.html')


def log_in(request):
    lnav = "active"
    return render(request, 'nhdo_main/login.html', {'lnav':lnav})


def home(request):
    nav1 = "active"
    nom = Profile.objects.all()
    if request.user.is_authenticated():
        referal_team(request)
        referal_counts(request)
        referal_level(request)
        summary(request)
        referral = Profile.objects.get(user=request.user)
        referral.your_referal = 'FFI/WSHG/RMD/' + request.user.username
        x = Profile.objects.all()
        referral.count1 = 0
        referral.count2 = 0
        referral.count3 = 0
        referral.count4 = 0
        referral.count5 = 0
        referral.count6 = 0
        referral.money = 0
        for i in x:
            if referral.your_referal == i.referal_id:
                referral.count1 = referral.count1 + 1
                for j in x:
                    if i.user.profile.your_referal == j.referal_id:
                        referral.count2 = referral.count2 + 1
                        for k in x:
                            if j.user.profile.your_referal == k.referal_id:
                                referral.count3 = referral.count3 + 1
                                for l in x:
                                    if k.user.profile.your_referal == l.referal_id:
                                        referral.count4 = referral.count4 + 1
                                        for m in x:
                                            if l.user.profile.your_referal == m.referal_id:
                                                referral.count5 = referral.count5 + 1
                                                for n in x:
                                                    if m.user.profile.your_referal == n.referal_id:
                                                        referral.count6 = referral.count6 + 1

        if referral.count1 >= 3:
            for i in x:
                if referral.your_referal == i.referal_id:
                    referral.money = referral.money + (0.1 * amount) #50
                    if i.user.profile.count1 >=3:
                        for j in x:
                            if i.user.profile.your_referal == j.referal_id:
                                referral.money = referral.money + (0.05 * amount) #25
                                if j.user.profile.count1 >= 3:
                                    for k in x:
                                        if j.user.profile.your_referal == k.referal_id:
                                            referral.money = referral.money + (0.04 * amount) #20
                                            if k.user.profile.count1 >= 3:
                                                for l in x:
                                                    if k.user.profile.your_referal == l.referal_id:
                                                        referral.money = referral.money + (0.03 * amount) #15
                                                        if l.user.profile.count1 >= 3:
                                                            for m in x:
                                                                if l.user.profile.your_referal == m.referal_id:
                                                                    referral.money = referral.money + (0.02 * amount) #10
                                                                    if m.user.profile.count1 >= 3:
                                                                        for n in x:
                                                                            if m.user.profile.your_referal == n.referal_id:
                                                                                referral.money = referral.money + (0.01 * amount) #5
        referral.total = referral.count1 + referral.count2 + referral.count3 + referral.count4 + referral.count5 + referral.count6
        referral.save()
        p = Profile.objects.all()
        return render(request, 'nhdo_main/index.html', {'info':p, 'nom':nom, 'nav1':nav1})
    else:
        return render(request, 'nhdo_main/index.html', {'nom':nom, 'nav1':nav1})


def referral_level(request):
    ref = Profile.objects.get(user=request.user)
    x = Profile.objects.all()
    return render(request, 'nhdo_main/referral_level.html', {'ref':ref, 'x':x})


def referral_level(request):
    level = Profile.objects.get(user=request.user)
    x = Profile.objects.all()
    return render(request, 'referral_level.html', {'x':x, 'level':level})


def about(request):
    nav2 = "active"
    return render(request, 'nhdo_main/about.html', {'nav2':nav2})


def women_empowerment(request):
    return render(request, 'nhdo_main/women_empowerment.html')


def ierp(request):
    return render(request, 'nhdo_main/ierp.html')


def mudra(request):
    return render(request, 'nhdo_main/mudra.html')


def shg(request):
    return render(request, 'nhdo_main/shg.html')


def pmkvy(request):
    return render(request, 'nhdo_main/pmkvy.html')


def standup(request):
    return render(request, 'nhdo_main/standup.html')


def garib_kalyan(request):
    return render(request, 'nhdo_main/garib_kalyan.html')


def makeinindia(request):
    return render(request, 'nhdo_main/makeinindia.html')


def smartcity(request):
    return render(request, 'nhdo_main/smartcity.html')


def project(request):
    return render(request, 'nhdo_main/project.html')


def gallery(request):
    nav3 = "active"
    return render(request, 'nhdo_main/gallery.html', {'nav3':nav3})


def contact(request):
    nav5 = "active"
    # n = Profile.objects.filter()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'nhdo_main/contact.html', {'form':form, 'nav5':nav5})


def change_password(request):
    value2 = "active"
    user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'nhdo_main/change_password.html', {'form': form, 'value2':value2})
