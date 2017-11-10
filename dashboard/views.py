from django.shortcuts import render, redirect
from nhdo_main.models import Profile
from .forms import EditForm, KycForm
from .models import kyc, Welcome, Distributor_agreement
from django.contrib.auth.models import User


def dashboard(request):
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
    referrar = Profile.objects.get(user=request.user)
    x = Profile.objects.all()
    return render(request, 'dashboard/referal_team.html', {'referrar': referrar, 'x': x, 'money': referrar.money, 'value6':value6})


def referal_counts(request):
    value7 = "active"
    referral = Profile.objects.get(user=request.user)
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


def referal_level(request):
    ref = Profile.objects.get(user=request.user)
    x = Profile.objects.all()
    value8 = "active"
    return render(request, 'dashboard/referal_level.html', {'referrar':ref, 'x':x, 'value8':value8})


def summary(request):
    value9 = "active"
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
    ac = Profile.objects.get(user=request.user)
    return render(request, 'dashboard/ac_statement.html', {'value10':value10, 'ac':ac})
