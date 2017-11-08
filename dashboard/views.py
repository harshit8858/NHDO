from django.shortcuts import render, redirect
from nhdo_main.models import Profile
from .forms import EditForm, KycForm
from .models import kyc, Welcome, Distributor_agreement
from django.contrib.auth.models import User
from nhdo_main.views import home


def dashboard(request):
    home(request)
    nom = Profile.objects.all()
    p = Profile.objects.all()
    value1 = "active"
    return render(request, 'dashboard/dashboard.html', {'info':p, 'nom':nom, 'value1':value1})


def edit_profile(request,d):
    n = Profile.objects.get(id=d)
    value1 = "active"
    if request.method == 'POST':
        form = EditForm(request.POST,request.FILES,instance=n)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditForm(instance=n)
    return render(request, 'dashboard/edit_profile.html', {'form':form, 'value1':value1})


def update_kyc(request):
    u = User.objects.all()
    i = kyc.objects.all()
    value3 = "active"
    return render(request, 'dashboard/update_kyc.html', {'pic':i,'u':u, 'value3':value3})


def add_kyc(request):
    value3 = "active"
    if request.method == 'POST':
        form = KycForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('update_kyc')
    else:
        form = KycForm()
    return render(request, 'dashboard/add_kyc.html', {'form':form, 'value3':value3})


def edit_kyc(request,d):
    value3 = "active"
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
    return render(request, 'dashboard/edit_kyc.html', {'form':form, 'value3':value3})


def welcome_letter(request):
    value4 = "active"
    wel = Welcome.objects.all()
    return render(request, 'dashboard/welcome_letter.html',{'wel':wel, 'value4':value4})


def distributer_agreement(request):
    value5 = "active"
    d_a = Distributor_agreement.objects.all()
    return render(request, 'dashboard/distributer_agreement.html', {'d_a':d_a, 'value5':value5})


def referal_team(request):
    value6 = "active"
    referal_counts(request)
    referal_level(request)
    summary(request)
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
    return render(request, 'dashboard/referal_team.html', {'referrar': referrar, 'x': x, 'money': referrar.money, 'value6':value6})


def referal_counts(request):
    value7 = "active"
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

    print(referral.money)
    if referral.count1 < 3:
        referral.level_reached = 0
    elif referral.count1 >= 3:
        referral.level_reached = 1
    elif referral.count2 >= 625:
        referral.level_reached = 2
    elif referral.count3 >= 15626:
        referral.level_reached = 3
    elif referral.count4 >= 390625:
        referral.level_reached = 4
    elif referral.count5 >= 9765625:
        referral.level_reached = 5
    elif referral.count1 >= 244140625:
        referral.level_reached = 6
    referral.save()

    count1per = float((referral.count1/25))*100
    count2per = float((referral.count2/625))*100
    count3per = float((referral.count3/15625))*100
    count4per = float((referral.count4/390625))*100
    count5per = float((referral.count5/9765625))*100
    count6per = float((referral.count6/244140625))*100
    return render(request, 'dashboard/referal_counts.html', {'referral': referral.your_referal,
                                                             'count1': referral.count1,
                                                             'count1per':count1per,
                                                             'count2': referral.count2,
                                                             'count2per':count2per,
                                                             'count3': referral.count3,
                                                             'count3per':count3per,
                                                             'count4': referral.count4,
                                                             'count4per':count4per,
                                                             'count5': referral.count5,
                                                             'count5per':count5per,
                                                             'count6': referral.count6,
                                                             'count6per':count6per,
                                                             'total': referral.total,
                                                             'level':referral.level_reached,
                                                             'value7':value7})
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
    value8 = "active"
    return render(request, 'dashboard/referal_level.html', {'referrar':ref, 'x':x, 'value8':value8})

#
# def direct_bonus(request):
#     return render(request, 'dashboard/direct_bonus.html', )


def summary(request):
    value9 = "active"
    home(request)
    summ = Profile.objects.get(user=request.user)
    if summ.level_reached == 0:
        summ.rest = 0
    elif summ.level_reached == 1:
        summ.rest = summ.money - 1250
    elif summ.level_reached == 2:
        summ.rest = summ.money - 15625 - 1250
    elif summ.level_reached == 3:
        summ.rest = summ.money - 312500 - 15625 - 1250
    elif summ.level_reached == 4:
        summ.rest = summ.money - 5859375 - 312500 - 15625 - 1250
    elif summ.level_reached == 5:
        summ.rest = summ.money - 97656250 - 5859375 - 312500 - 15625 - 1250
    elif summ.level_reached == 6:
        summ.rest = 0
    summ.save()

    return render(request, 'dashboard/summary.html', {'money': summ.money, 'level':summ.level_reached, 'value9':value9, 'rest':summ.rest})


def ac_statement(request):
    value10 = "active"
    home(request)
    return render(request, 'dashboard/ac_statement.html', {'value10':value10})
