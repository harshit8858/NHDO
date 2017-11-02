from django.shortcuts import render, redirect
from nhdo_main.models import Profile
from .forms import EditForm, EditForm1, Epin_upgradeForm, KycForm
from .models import Epin, kyc, Welcome, Distributor_agreement
from django.contrib.auth.models import User
from nhdo_main.views import home


def dashboard(request):
    home(request)
    p = Profile.objects.all()
    return render(request, 'dashboard/dashboard.html', {'info':p})


def edit_profile(request,d):
    n = Profile.objects.get(id=d)
    if request.method == 'POST':
        form = EditForm(request.POST,request.FILES,instance=n)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditForm(instance=n)
    return render(request, 'dashboard/edit_profile.html', {'form':form})


def edit_profile1(request,d):
    n = User.objects.get(id=d)
    if request.method == 'POST':
        form = EditForm1(request.POST, instance=n)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditForm1(instance=n)
    return render(request, 'dashboard/edit_profile1.html', {'form':form})


def list_epin(request):
    home(request)
    return render(request, 'dashboard/list_epins.html', )


def upgrade_account(request):
    home(request)
    if request.method == 'POST':
        form = Epin_upgradeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('dashboard')
    else:
        form = Epin_upgradeForm()
    return render(request, 'dashboard/upgrade_account.html', {'form':form})


def update_kyc(request):
    u = User.objects.all()
    i = kyc.objects.all()
    return render(request, 'dashboard/update_kyc.html', {'pic':i,'u':u})


def add_kyc(request):
    if request.method == 'POST':
        form = KycForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('update_kyc')
    else:
        form = KycForm()
    return render(request, 'dashboard/add_kyc.html', {'form':form})


def edit_kyc(request,d):
    n = kyc.objects.get(id=d)
    if request.method == 'POST':
        form = KycForm(request.POST, request.FILES, instance=n)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('update_kyc')
    else:
        form = KycForm(instance=n)
    return render(request, 'dashboard/edit_kyc.html', {'form':form})


def welcome_letter(request):
    wel = Welcome.objects.all()
    return render(request, 'dashboard/welcome_letter.html',{'wel':wel})


def distributer_agreement(request):
    d_a = Distributor_agreement.objects.all()
    return render(request, 'dashboard/distributer_agreement.html', {'d_a':d_a})


def referal_team(request):
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
    return render(request, 'dashboard/referal_team.html', {'referrar': referrar, 'x': x, 'money': referrar.money})


def referal_counts(request):
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
    if referral.count1 < 3:
        referral.level_reached = 0
    elif referral.count1 > 3:
        referral.level_reached = 1
    elif referral.count2 > 625:
        referral.level_reached = 2
    elif referral.count3 > 15626:
        referral.level_reached = 3
    elif referral.count4 > 390625:
        referral.level_reached = 4
    elif referral.count5 > 9765625:
        referral.level_reached = 5
    elif referral.count1 > 244140625:
        referral.level_reached = 6
    referral.save()

    return render(request, 'dashboard/referal_counts.html', {'referral': referral.your_referal,
                                                            'count1': referral.count1,
                                                            'count2': referral.count2,
                                                            'count3': referral.count3,
                                                            'count4': referral.count4,
                                                            'count5': referral.count5,
                                                            'count6': referral.count6,
                                                            'total': referral.total,
                                                            'level':referral.level_reached})
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


def referal_level(request):
    home(request)
    ref = Profile.objects.get(user=request.user)
    x = Profile.objects.all()
    return render(request, 'dashboard/referal_level.html', {'referrar':ref, 'x':x})


def direct_bonus(request):
    return render(request, 'dashboard/direct_bonus.html', )


def summary(request):
    home(request)
    summary = Profile.objects.get(user=request.user)
    level1_income = summary.count2 * 50
    level2_income = summary.count2 * 20
    level3_income = summary.count3 * 25
    level4_income = summary.count4 * 12.5
    level5_income = summary.count2 * 50
    level6_income = summary.count2 * 50
    total = + level1_income + level2_income + level3_income + level4_income + level5_income + level6_income

    return render(request, 'dashboard/summary.html', {'total':total})


def ac_statement(request):
    home(request)
    return render(request, 'dashboard/ac_statement.html', )
