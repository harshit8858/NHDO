from django.shortcuts import render, redirect
from nhdo_main.models import Profile
from .forms import EditForm, Epin_upgradeForm, KycForm, EditForm1
from .models import Epin, kyc
from django.contrib.auth.models import User


def dashboard(request):
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
        form = EditForm1(request.POST,request.FILES,instance=n)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditForm1(instance=n)
    return render(request, 'dashboard/edit_profile.html', {'form':form})


def list_epin(request):
    return render(request, 'dashboard/list_epins.html', )


def upgrade_account(request):
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
    i = kyc.objects.all()
    return render(request, 'dashboard/update_kyc.html', {'pic':i})


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
    return render(request, 'dashboard/welcome_letter.html', )


def distributer_agreement(request):
    return render(request, 'dashboard/distributer_agreement.html', )


def geneology_team(request):
    return render(request, 'dashboard/geneology_team.html', )


def referal_team(request):
    return render(request, 'dashboard/referal_team.html', )


def downline_team(request):
    return render(request, 'dashboard/downline_team.html', )


def direct_bonus(request):
    return render(request, 'dashboard/direct_bonus.html', )


def summary(request):
    return render(request, 'dashboard/summary.html', )


def ac_statement(request):
    return render(request, 'dashboard/ac_statement.html', )


def compose(request):
    return render(request, 'dashboard/compose.html', )