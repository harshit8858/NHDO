from django.http import HttpResponseRedirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import ContactForm
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
# from django.core.mail import EmailMessage
# from pinax.referrals.models import Referral
# import pinax
from django.contrib.auth.models import User
from django.db.models import F


def index(request):
    # email = EmailMessage('title', 'body', to=['dk291996@gmail.com'])
    # abc = email.send()
    # print (abc)
    return render(request, 'nhdo_main/index.html')


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
            # referral = Referral.create(
            #     user=user,
            #     redirect_to=reverse("index")
            # )
            # Profile.referral = referral
            # print("h")
            # Profile.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'nhdo_main/signup.html', {'form':form})


def your_referral(request):
    home(request)
    referral = Profile.objects.get(user=request.user)
    # x = Profile.objects.all()
    # y = Profile.objects.values_list('referal_id', flat=True)
    # # print(x)
    # # print(y)
    # # print(referral.mobile_number)
    # referral.count = 0
    # referral.count1 = 0
    # referral.count2 = 0
    # referral.count3 = 0
    # for i in x:
    #     if referral.mobile_number == i.referal_id:
    #         a = i.user.first_name
    #         referral.count = referral.count + 1
    #         referral.save()
    #         # print('a')
    #         # print(a)
    #         for j in x:
    #             if i.user.profile.mobile_number == j.referal_id:
    #                 b = j.user.first_name
    #                 referral.count1 = referral.count1 + 1
    #                 referral.save()
    #                 # print('b')
    #                 # print(b)
    #                 for k in x:
    #                     if j.user.profile.mobile_number == k.referal_id:
    #                         c = k.user.first_name
    #                         referral.count2 = referral.count2 + 1
    #                         referral.save()
    #                         # print('c')
    #                         # print(c)
    #                         for l in x:
    #                             if k.user.profile.mobile_number == l.referal_id:
    #                                 # print('d')
    #                                 # d = l.user.first_name
    #                                 referral.count3 = referral.count3 + 1
    #                                 # print(referral.count3)
    #                                 referral.save()
    return render(request, 'nhdo_main/your_referral.html',{'referral':referral.mobile_number,
                                                           'count':referral.count,
                                                           'count1':referral.count1,
                                                           'count2':referral.count2,
                                                           'count3':referral.count3})
#     referral = Profile.objects.get(user=request.user)
#     # print(referral)
#     # print(referral.referal_id)
#     y = Profile.objects.values_list('referal_id', flat=True)
#     z = User.objects.values_list('username', flat=True)
#     x = Profile.objects.all()
#     print(x)
#     a = len(y)
#     i = 0
#     j = 0
#     k = 0
#     l = 0
#     # print(referral.count1)
#     # print(referral.count2)
#     # print(referral.count3)
#     while i < a:
#         if referral.mobile_number == y[i]:
#             r = referral.id
#             # print(r)
#             # print(b)
#             p = referral.count
#             p = p + 1
#             referral.count = p
#             # print('p')
#             # print(p)
#             # print('p')
#
#             while j < a:
#                 # if i.user.profile.mobile_number == j.referal_id:
#                 if y[i] == y[j]:
#                     q = referral.count1
#                     q = q + 1
#                     referral.count1 = q
#                     # print('q')
#                     # print(q)
#                     # print('q')
#
#                     while k < a:
#                         if y[j] == y[k]:
#                             r = referral.count1
#                             r = r + 1
#                             referral.count2 = r
#                             # print('r')
#                             # print(r)
#                             # print('r')
#
#                             while l < a:
#                                 if y[k] == y[l]:
#                                     s = referral.count1
#                                     s = s + 1
#                                     referral.count3 = s
#                                     # print('s')
#                                     # print(s)
#                                     # print('s')
#                                 l = l + 1
#                         k = k + 1
#                 j = j + 1
#         i = i + 1
#     print("p:" + str(p))
#     print("q:" + str(q))
#     print("r:" + str(r))
#     print("s:" + str(s))
#     # form = ReferralForm()
#     # f = form.save()
#     # f.user = request.user
#     # f.count = referral.count
#     # f.save()
#     # referral.save(['count'])
#     # n = Profile.objects.get(id=d)
#     # form = SignUpForm(instance=n)
#     # f = form.save(commit=False)
#     # # f.user = request.user
#     # f.count = x.count
#     # f.save()
#     return render(request, 'your_referral.html', {'referral':referral.mobile_number, 'count':referral.count, 'count1':referral.count1, 'count2':referral.count2, 'count3':referral.count3})


def your_referrar(request):
    home(request)
    referrar = Profile.objects.get(user=request.user)
    x = Profile.objects.all()
    # y = Profile.objects.values_list('referal_id', flat=True)
    # # print(x)
    # # print(y)
    # # print(referrar.mobile_number)
    # referrar.money = 0
    # for i in x:
    #     if referrar.mobile_number == i.referal_id:
    #         # a = i.user.first_name
    #         referrar.money = referrar.money + 100
    #         # print('a')
    #         # print(a)
    #         direct = i.user
    #         # print('direct:' + str(direct))
    #         for j in x:
    #             # print("asasasasa:" + str(i.user))
    #             if i.user.profile.mobile_number == j.referal_id:
    #                 # b = j.user.first_name
    #                 referrar.money = referrar.money + 50
    #                 # print('b')
    #                 # print(b)
    #                 level1 = j.user
    #                 # print('level1:' + str(level1))
    #                 for k in x:
    #                     if j.user.profile.mobile_number == k.referal_id:
    #                         # c = k.user.first_name
    #                         referrar.money = referrar.money + 25
    #                         # print('c')
    #                         # print(c)
    #                         level2 = k.user
    #                         # print('level2:' + str(level2))
    #                         for l in x:
    #                             if k.user.profile.mobile_number == l.referal_id:
    #                                 # print('d')
    #                                 # print(d)
    #                                 # d = l.user.first_name
    #                                 referrar.money = referrar.money + 12.5
    #                                 level3 = l.user
    #                                 # print('level3:' + str(level3))
    #     referrar.save()

    # return render(request, 'your_referrar.html', {'referrar':referrar, 'x':x, 'y':y, 'a':a, 'b':b, 'c':c, 'money':referrar.money})
    return render(request, 'nhdo_main/your_referrar.html', {'referrar':referrar, 'x':x, 'money':referrar.money})


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
    return render(request, 'nhdo_main/login.html')


def home(request):
    if request.user.is_authenticated():
        referral = Profile.objects.get(user=request.user)
        x = Profile.objects.all()
        y = Profile.objects.values_list('referal_id', flat=True)
        referral.count = 0
        referral.count1 = 0
        referral.count2 = 0
        referral.count3 = 0
        referral.money = 0
        for i in x:
            if referral.mobile_number == i.referal_id:
                referral.money = referral.money + 100
                referral.count = referral.count + 1
                for j in x:
                    if i.user.profile.mobile_number == j.referal_id:
                        referral.money = referral.money + 50
                        referral.count1 = referral.count1 + 1
                        for k in x:
                            if j.user.profile.mobile_number == k.referal_id:
                                referral.money = referral.money + 25
                                referral.count2 = referral.count2 + 1
                                for l in x:
                                    if k.user.profile.mobile_number == l.referal_id:
                                        referral.money = referral.money + 12.5
                                        referral.count3 = referral.count3 + 1
        referral.total = referral.count + referral.count1 + referral.count2 + referral.count3
        referral.save()
        # print(referral.count)
        # print(referral.count1)
        # print(referral.count2)
        # print(referral.count3)
        # print(referral.money)
        return render(request, 'nhdo_main/home.html')
    else:
        return render(request, 'nhdo_main/invalid.html')


def referral_level(request):
    ref = Profile.objects.get(user=request.user)
    x = Profile.objects.all()
    return render(request, 'nhdo_main/referral_level.html', {'ref':ref, 'x':x})


def about(request):
    return render(request, 'nhdo_main/about.html')


def project(request):
    return render(request, 'nhdo_main/project.html')


def gallery(request):
    return render(request, 'nhdo_main/gallery.html')


def contact(request):
    # n = Profile.objects.filter()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'nhdo_main/contact.html', {'form':form})


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
    return render(request, 'nhdo_main/change_password.html', {'form': form})


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